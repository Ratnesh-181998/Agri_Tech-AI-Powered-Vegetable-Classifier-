import os

# Base Directories
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, 'ninjacart_data')
TRAIN_DIR = os.path.join(DATA_DIR, 'train')
TEST_DIR = os.path.join(DATA_DIR, 'test')

# Model Artifacts
MODELS_DIR = os.path.join(BASE_DIR, 'backend', 'saved_models')
CLASS_INDICES_PATH = os.path.join(MODELS_DIR, 'class_indices.json')
METRICS_PATH = os.path.join(MODELS_DIR, 'model_metrics.json')

# Logging
LOGS_DIR = os.path.join(BASE_DIR, 'backend', 'logs')
LOG_FILE = os.path.join(LOGS_DIR, 'app.log')

# Training Settings
IMG_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 5
MODELS_TO_TRAIN = ['ann', 'cnn', 'mobilenet', 'vgg19', 'resnet50']

# Ensure directories exist
os.makedirs(MODELS_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)
