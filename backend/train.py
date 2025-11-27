import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from model import get_model_factory
import json
import matplotlib.pyplot as plt

# Configuration
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ninjacart_data')
TRAIN_DIR = os.path.join(DATA_DIR, 'train')
TEST_DIR = os.path.join(DATA_DIR, 'test')
IMG_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 5
CLASS_INDICES_PATH = 'class_indices.json'
METRICS_PATH = 'model_metrics.json'

MODELS_TO_TRAIN = ['ann', 'cnn', 'mobilenet', 'vgg19', 'resnet50']

def train():
    if not os.path.exists(TRAIN_DIR):
        print(f"Error: Training directory not found at {TRAIN_DIR}")
        return

    # Data Augmentation
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )

    test_datagen = ImageDataGenerator(rescale=1./255)

    print("Loading training data...")
    train_generator = train_datagen.flow_from_directory(
        TRAIN_DIR,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical'
    )

    print("Loading validation data...")
    validation_generator = test_datagen.flow_from_directory(
        TEST_DIR,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical'
    )

    num_classes = len(train_generator.class_indices)
    print(f"Detected {num_classes} classes: {train_generator.class_indices}")

    # Save class indices
    with open(CLASS_INDICES_PATH, 'w') as f:
        json.dump(train_generator.class_indices, f)

    metrics_data = {}

    for model_name in MODELS_TO_TRAIN:
        print(f"\n{'='*50}")
        print(f"Training {model_name.upper()} Model...")
        print(f"{'='*50}")

        create_fn = get_model_factory(model_name)
        if not create_fn:
            print(f"Unknown model: {model_name}")
            continue

        model = create_fn(num_classes)
        
        history = model.fit(
            train_generator,
            steps_per_epoch=train_generator.samples // BATCH_SIZE,
            epochs=EPOCHS,
            validation_data=validation_generator,
            validation_steps=validation_generator.samples // BATCH_SIZE
        )

        # Save model
        model_filename = f"model_{model_name}.h5"
        model.save(model_filename)
        print(f"Saved {model_name} model to {model_filename}")

        # Store metrics
        final_acc = history.history['accuracy'][-1]
        final_val_acc = history.history['val_accuracy'][-1]
        final_loss = history.history['loss'][-1]
        final_val_loss = history.history['val_loss'][-1]

        metrics_data[model_name] = {
            'accuracy': float(final_acc),
            'val_accuracy': float(final_val_acc),
            'loss': float(final_loss),
            'val_loss': float(final_val_loss)
        }

    # Save metrics
    with open(METRICS_PATH, 'w') as f:
        json.dump(metrics_data, f, indent=4)
    print(f"\nAll training complete. Metrics saved to {METRICS_PATH}")

if __name__ == '__main__':
    train()
