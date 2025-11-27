import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
    return (
        <div className="ninjacart-home">
            {/* Hero Section */}
            <section className="hero-section">
                <div className="hero-container">
                    <div className="hero-text">
                        <h1>
                            India's Most Advanced<br />
                            <span className="highlight">AI Vegetable Classifier</span>
                        </h1>
                        <p>
                            Powered by deep learning technology to identify fresh produce instantly with 93%+ accuracy
                        </p>
                        <div className="hero-buttons">
                            <Link to="/classifier" className="btn btn-primary">Try Classifier</Link>
                            <Link to="/vegetables" className="btn btn-outline">View All Vegetables</Link>
                        </div>
                    </div>
                    <div className="hero-visual">
                        <div className="visual-grid">
                            <div className="visual-item">🍅</div>
                            <div className="visual-item">🥔</div>
                            <div className="visual-item">🧅</div>
                            <div className="visual-item">🥕</div>
                            <div className="visual-item">🥦</div>
                            <div className="visual-item">🌽</div>
                        </div>
                    </div>
                </div>
            </section>

            {/* Features Section */}
            <section className="features-section">
                <div className="container">
                    <div className="section-title">
                        <h2>Why Choose Our AI Classifier?</h2>
                        <p>State-of-the-art technology for accurate vegetable recognition</p>
                    </div>
                    <div className="features-grid">
                        <div className="feature-card">
                            <div className="feature-icon">⚡</div>
                            <h3>Lightning Fast</h3>
                            <p>Get results in under 1 second with our optimized models</p>
                        </div>
                        <div className="feature-card">
                            <div className="feature-icon">🎯</div>
                            <h3>High Accuracy</h3>
                            <p>93%+ accuracy across all trained vegetable categories</p>
                        </div>
                        <div className="feature-card">
                            <div className="feature-icon">🧠</div>
                            <h3>5 AI Models</h3>
                            <p>Compare ANN, CNN, VGG19, ResNet50, MobileNetV2</p>
                        </div>
                        <div className="feature-card">
                            <div className="feature-icon">📊</div>
                            <h3>Real-time Analytics</h3>
                            <p>View confidence scores and training metrics</p>
                        </div>
                    </div>
                </div>
            </section>

            {/* Categories Section */}
            <section className="categories-section">
                <div className="container">
                    <div className="section-title">
                        <h2>Available Categories</h2>
                        <p>Currently supporting 4 vegetable types with more coming soon</p>
                    </div>
                    <div className="categories-grid">
                        <div className="category-card">
                            <div className="category-icon">🍅</div>
                            <h3>Tomato</h3>
                            <span className="badge badge-success">Available Now</span>
                        </div>
                        <div className="category-card">
                            <div className="category-icon">🥔</div>
                            <h3>Potato</h3>
                            <span className="badge badge-success">Available Now</span>
                        </div>
                        <div className="category-card">
                            <div className="category-icon">🧅</div>
                            <h3>Onion</h3>
                            <span className="badge badge-success">Available Now</span>
                        </div>
                        <div className="category-card">
                            <div className="category-icon">🏪</div>
                            <h3>Indian Market</h3>
                            <span className="badge badge-success">Available Now</span>
                        </div>
                    </div>
                </div>
            </section>

            {/* Stats Section */}
            <section className="stats-section">
                <div className="stats-grid">
                    <div className="stat-item">
                        <h3>3,135</h3>
                        <p>Training Images</p>
                    </div>
                    <div className="stat-item">
                        <h3>5</h3>
                        <p>AI Models</p>
                    </div>
                    <div className="stat-item">
                        <h3>93%+</h3>
                        <p>Accuracy</p>
                    </div>
                    <div className="stat-item">
                        <h3>&lt;1s</h3>
                        <p>Response Time</p>
                    </div>
                </div>
            </section>

            {/* CTA Section */}
            <section className="cta-section">
                <div className="cta-content">
                    <h2>Ready to Try Our AI Classifier?</h2>
                    <p>Upload an image and get instant vegetable classification</p>
                    <Link to="/classifier" className="btn btn-primary">Get Started Now →</Link>
                </div>
            </section>
        </div>
    );
};

export default Home;
