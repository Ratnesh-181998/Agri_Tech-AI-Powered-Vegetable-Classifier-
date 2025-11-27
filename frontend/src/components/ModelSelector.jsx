import React from 'react';

const ModelSelector = ({ selectedModel, onSelectModel }) => {
    const models = [
        { id: 'mobilenet', name: 'MobileNetV2', desc: 'Fastest' },
        { id: 'ann', name: 'ANN', desc: 'Simple' },
        { id: 'cnn', name: 'Custom CNN', desc: 'Balanced' },
        { id: 'vgg19', name: 'VGG19', desc: 'High Accuracy' },
        { id: 'resnet50', name: 'ResNet50', desc: 'Powerful' }
    ];

    return (
        <div className="model-selector">
            <span className="model-label">Select AI Architecture</span>
            <div className="model-grid">
                {models.map(model => (
                    <div
                        key={model.id}
                        className={`model-card ${selectedModel === model.id ? 'active' : ''}`}
                        onClick={() => onSelectModel(model.id)}
                    >
                        <div>{model.name}</div>
                        <div style={{ fontSize: '0.7rem', opacity: 0.7, marginTop: '5px' }}>{model.desc}</div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default ModelSelector;
