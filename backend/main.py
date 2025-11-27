from fastapi import FastAPI, File, UploadFile, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import io
import json
import os

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CLASS_INDICES_PATH = 'class_indices.json'
METRICS_PATH = 'model_metrics.json'

# Cache for loaded models
loaded_models = {}
class_names = None

def get_model_path(model_name):
    return f"model_{model_name}.h5"

@app.on_event("startup")
async def startup_event():
    global class_names
    
    # Load class indices
    if os.path.exists(CLASS_INDICES_PATH):
        with open(CLASS_INDICES_PATH, 'r') as f:
            indices = json.load(f)
            class_names = {v: k for k, v in indices.items()}
            print(f"Class indices loaded: {class_names}")
    else:
        print("Class indices file not found.")

    # Pre-load default model (mobilenet)
    load_ai_model('mobilenet')

def load_ai_model(model_name):
    if model_name in loaded_models:
        return loaded_models[model_name]
    
    path = get_model_path(model_name)
    if os.path.exists(path):
        try:
            print(f"Loading model: {model_name}...")
            model = load_model(path)
            loaded_models[model_name] = model
            print(f"Model {model_name} loaded successfully.")
            return model
        except Exception as e:
            print(f"Error loading model {model_name}: {e}")
            return None
    else:
        print(f"Model file {path} not found.")
        return None

@app.get("/")
async def root():
    return {"message": "Ninjacart CV Classification API is running"}

@app.get("/models")
async def get_models_info():
    """Return available models and their metrics"""
    if os.path.exists(METRICS_PATH):
        with open(METRICS_PATH, 'r') as f:
            metrics = json.load(f)
        return metrics
    return {"error": "No model metrics found. Please run training first."}

@app.post("/predict")
async def predict(
    file: UploadFile = File(...), 
    model_type: str = Query('mobilenet', description="Model to use: ann, cnn, mobilenet, vgg19, resnet50")
):
    global class_names
    
    model = load_ai_model(model_type)
    
    if model is None:
        return {
            "class": "Error",
            "confidence": 0.0,
            "message": f"Model '{model_type}' not found or failed to load. Please train it first."
        }
        
    if class_names is None:
        return {
            "class": "Error",
            "confidence": 0.0,
            "message": "Class indices not found."
        }

    try:
        # Read and preprocess image
        contents = await file.read()
        img = Image.open(io.BytesIO(contents))
        img = img.resize((224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0

        # Predict
        predictions = model.predict(img_array)
        predicted_class_index = np.argmax(predictions[0])
        confidence = float(predictions[0][predicted_class_index])
        predicted_class = class_names.get(predicted_class_index, "Unknown")

        return {
            "model": model_type,
            "class": predicted_class,
            "confidence": confidence
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
