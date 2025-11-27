from fastapi import APIRouter, File, UploadFile, HTTPException, Query
from tensorflow.keras.models import load_model
import numpy as np
import json
import os
from app.config import MODELS_DIR, CLASS_INDICES_PATH, METRICS_PATH
from app.utils.image import preprocess_image
from app.utils.logger import logger

router = APIRouter()

# Cache for loaded models
loaded_models = {}
class_names = None

def get_model_path(model_name):
    return os.path.join(MODELS_DIR, f"model_{model_name}.h5")

def load_ai_model(model_name):
    if model_name in loaded_models:
        return loaded_models[model_name]
    
    path = get_model_path(model_name)
    if os.path.exists(path):
        try:
            logger.info(f"Loading model: {model_name}...")
            model = load_model(path)
            loaded_models[model_name] = model
            logger.info(f"Model {model_name} loaded successfully.")
            return model
        except Exception as e:
            logger.error(f"Error loading model {model_name}: {e}")
            return None
    else:
        logger.warning(f"Model file {path} not found.")
        return None

@router.on_event("startup")
async def startup_event():
    global class_names
    
    # Load class indices
    if os.path.exists(CLASS_INDICES_PATH):
        with open(CLASS_INDICES_PATH, 'r') as f:
            indices = json.load(f)
            class_names = {v: k for k, v in indices.items()}
            logger.info(f"Class indices loaded: {class_names}")
    else:
        logger.error("Class indices file not found.")

    # Pre-load default model
    load_ai_model('mobilenet')

@router.get("/")
async def root():
    logger.info("Root endpoint accessed")
    return {"message": "Ninjacart CV Classification API is running"}

@router.get("/models")
async def get_models_info():
    """Return available models and their metrics"""
    logger.info("Fetching models info")
    if os.path.exists(METRICS_PATH):
        with open(METRICS_PATH, 'r') as f:
            metrics = json.load(f)
        return metrics
    logger.warning("No model metrics found")
    return {"error": "No model metrics found. Please run training first."}

@router.post("/predict")
async def predict(
    file: UploadFile = File(...), 
    model_type: str = Query('mobilenet', description="Model to use: ann, cnn, mobilenet, vgg19, resnet50")
):
    global class_names
    
    logger.info(f"Prediction request received for model: {model_type}")
    model = load_ai_model(model_type)
    
    if model is None:
        logger.error(f"Model '{model_type}' failed to load")
        return {
            "class": "Error",
            "confidence": 0.0,
            "message": f"Model '{model_type}' not found or failed to load. Please train it first."
        }
        
    if class_names is None:
        logger.error("Class indices not available")
        return {
            "class": "Error",
            "confidence": 0.0,
            "message": "Class indices not found."
        }

    try:
        # Read and preprocess image
        contents = await file.read()
        img_array = preprocess_image(contents)

        # Predict
        predictions = model.predict(img_array)
        predicted_class_index = np.argmax(predictions[0])
        confidence = float(predictions[0][predicted_class_index])
        predicted_class = class_names.get(predicted_class_index, "Unknown")

        logger.info(f"Prediction result: {predicted_class} ({confidence:.2f})")
        return {
            "model": model_type,
            "class": predicted_class,
            "confidence": confidence
        }

    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/analytics/{model_name}/plot")
async def get_training_plot(model_name: str):
    """Serve the training accuracy/loss plot for a specific model"""
    plot_path = os.path.join(MODELS_DIR, f'{model_name}_training_plot.png')
    if os.path.exists(plot_path):
        from fastapi.responses import FileResponse
        return FileResponse(plot_path)
    return {"error": "Plot not found. Model might not be trained yet."}
