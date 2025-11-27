import os
import time
from datetime import datetime

MODELS_DIR = 'saved_models'
MODELS = ['ann', 'cnn', 'mobilenet', 'vgg19', 'resnet50']

print("=" * 60)
print("NINJACART MODEL TRAINING MONITOR")
print("=" * 60)
print(f"Monitoring: {os.path.abspath(MODELS_DIR)}")
print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 60)

for model_name in MODELS:
    model_file = os.path.join(MODELS_DIR, f'model_{model_name}.h5')
    plot_file = os.path.join(MODELS_DIR, f'{model_name}_training_plot.png')
    
    model_exists = os.path.exists(model_file)
    plot_exists = os.path.exists(plot_file)
    
    status = "✅ COMPLETE" if (model_exists and plot_exists) else \
             "🔄 TRAINING" if model_exists else \
             "⏳ PENDING"
    
    size = ""
    if model_exists:
        size_mb = os.path.getsize(model_file) / (1024 * 1024)
        size = f"({size_mb:.1f} MB)"
    
    print(f"{model_name.upper():12} {status:15} {size}")

print("=" * 60)

# Check for metrics file
metrics_file = os.path.join(MODELS_DIR, 'model_metrics.json')
if os.path.exists(metrics_file):
    print("\n📊 Metrics file exists - Training may be complete!")
    with open(metrics_file, 'r') as f:
        import json
        metrics = json.load(f)
        print(f"\nTrained models: {', '.join(metrics.keys())}")
else:
    print("\n⏳ Training still in progress...")
