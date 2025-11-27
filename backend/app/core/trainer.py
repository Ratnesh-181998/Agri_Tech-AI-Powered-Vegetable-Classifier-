import os
import json
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, TensorBoard
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
from app.core.models import get_model_factory
from app.config import (
    TRAIN_DIR, TEST_DIR, IMG_SIZE, BATCH_SIZE, EPOCHS,
    MODELS_DIR, CLASS_INDICES_PATH, METRICS_PATH, MODELS_TO_TRAIN, LOGS_DIR
)
from app.utils.logger import logger

def plot_history(history, model_name):
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs_range = range(len(acc))

    plt.figure(figsize=(12, 4))
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, acc, label='Training Accuracy')
    plt.plot(epochs_range, val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.title(f'{model_name} Accuracy')

    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.title(f'{model_name} Loss')
    
    plot_path = os.path.join(MODELS_DIR, f'{model_name}_training_plot.png')
    plt.savefig(plot_path)
    plt.close()
    return plot_path

def train_all_models():
    logger.info("Starting rigorous training process...")
    if not os.path.exists(TRAIN_DIR):
        logger.error(f"Training directory not found at {TRAIN_DIR}")
        return

    # Data Augmentation with Validation Split (80-20)
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest',
        validation_split=0.2  # 20% validation split
    )

    # Test Data Generator (for final evaluation)
    test_datagen = ImageDataGenerator(rescale=1./255)

    logger.info("Loading training data (80%)...")
    train_generator = train_datagen.flow_from_directory(
        TRAIN_DIR,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='training'
    )

    logger.info("Loading validation data (20%)...")
    validation_generator = train_datagen.flow_from_directory(
        TRAIN_DIR,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='validation'
    )

    logger.info("Loading test data (Hold-out set)...")
    test_generator = test_datagen.flow_from_directory(
        TEST_DIR,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        shuffle=False # Important for confusion matrix
    )

    num_classes = len(train_generator.class_indices)
    logger.info(f"Detected {num_classes} classes: {train_generator.class_indices}")

    # Save class indices
    with open(CLASS_INDICES_PATH, 'w') as f:
        json.dump(train_generator.class_indices, f)

    metrics_data = {}

    for model_name in MODELS_TO_TRAIN:
        logger.info(f"\nTraining {model_name.upper()} Model...")

        create_fn = get_model_factory(model_name)
        if not create_fn:
            logger.warning(f"Unknown model: {model_name}")
            continue

        model = create_fn(num_classes)
        
        # Callbacks
        model_path = os.path.join(MODELS_DIR, f"model_{model_name}.h5")
        callbacks = [
            EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True),
            ModelCheckpoint(model_path, monitor='val_accuracy', save_best_only=True),
            TensorBoard(log_dir=os.path.join(LOGS_DIR, f'tensorboard_{model_name}'))
        ]

        history = model.fit(
            train_generator,
            steps_per_epoch=train_generator.samples // BATCH_SIZE,
            epochs=EPOCHS,
            validation_data=validation_generator,
            validation_steps=validation_generator.samples // BATCH_SIZE,
            callbacks=callbacks
        )

        # Generate Training Plots
        plot_path = plot_history(history, model_name)
        logger.info(f"Training plot saved to {plot_path}")

        # Final Evaluation on Test Set
        logger.info(f"Evaluating {model_name} on Test Set...")
        test_loss, test_acc = model.evaluate(test_generator)
        
        # Confusion Matrix
        predictions = model.predict(test_generator)
        y_pred = np.argmax(predictions, axis=1)
        y_true = test_generator.classes
        
        cm = confusion_matrix(y_true, y_pred)
        cm_dict = cm.tolist() # Convert to list for JSON serialization

        metrics_data[model_name] = {
            'accuracy': float(test_acc),
            'loss': float(test_loss),
            'confusion_matrix': cm_dict,
            'training_acc': [float(x) for x in history.history['accuracy']],
            'validation_acc': [float(x) for x in history.history['val_accuracy']]
        }
        logger.info(f"{model_name} Test Accuracy: {test_acc:.4f}")

    # Save metrics
    with open(METRICS_PATH, 'w') as f:
        json.dump(metrics_data, f, indent=4)
    logger.info(f"All training complete. Metrics saved to {METRICS_PATH}")
