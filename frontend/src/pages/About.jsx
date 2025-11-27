import React from 'react';

const About = () => {
    return (
        <div className="page-container">
            <div className="about-section">
                <h1 className="page-title">About Ninjacart CV Classification</h1>

                <div className="about-content">
                    <section className="about-block">
                        <h2>🎯 Problem Statement</h2>
                        <p>
                            Ninjacart is India's largest fresh produce supply chain company.
                            This project develops robust classifiers to distinguish between images
                            of different vegetables (onions, potatoes, tomatoes) while correctly
                            labeling non-vegetable images as noise.
                        </p>
                    </section>

                    <section className="about-block">
                        <h2>📊 Dataset</h2>
                        <ul>
                            <li><strong>Training:</strong> 3,135 images (Tomato: 789, Potato: 898, Onion: 849, Market: 599)</li>
                            <li><strong>Testing:</strong> 351 images (Tomato: 106, Potato: 83, Onion: 81, Market: 81)</li>
                            <li><strong>Source:</strong> Web-scraped from Google</li>
                        </ul>
                    </section>

                    <section className="about-block">
                        <h2>🧠 AI Models</h2>
                        <div className="models-grid">
                            <div className="model-info">
                                <h3>ANN</h3>
                                <p>Simple fully-connected neural network</p>
                            </div>
                            <div className="model-info">
                                <h3>CNN</h3>
                                <p>Custom convolutional architecture</p>
                            </div>
                            <div className="model-info">
                                <h3>VGG19</h3>
                                <p>Transfer learning with VGG19</p>
                            </div>
                            <div className="model-info">
                                <h3>ResNet50</h3>
                                <p>Deep residual network</p>
                            </div>
                            <div className="model-info">
                                <h3>MobileNetV2</h3>
                                <p>Lightweight and fast</p>
                            </div>
                        </div>
                    </section>

                    <section className="about-block">
                        <h2>⚙️ Technical Stack</h2>
                        <ul>
                            <li><strong>Backend:</strong> FastAPI, TensorFlow/Keras</li>
                            <li><strong>Frontend:</strong> React.js, Vite</li>
                            <li><strong>Features:</strong> Data Augmentation, Callbacks, Transfer Learning</li>
                        </ul>
                    </section>
                </div>
            </div>
        </div>
    );
};

export default About;
