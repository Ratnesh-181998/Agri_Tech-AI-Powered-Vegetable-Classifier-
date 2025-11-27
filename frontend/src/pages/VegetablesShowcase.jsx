import React from 'react';
import { Link } from 'react-router-dom';

const vegetables = [
    { name: 'Tomato', emoji: '🍅', color: '#ff6b6b', trained: true },
    { name: 'Potato', emoji: '🥔', color: '#d4a574', trained: true },
    { name: 'Onion', emoji: '🧅', color: '#e8c5a5', trained: true },
    { name: 'Indian Market', emoji: '🏪', color: '#4CAF50', trained: true },
    { name: 'Carrot', emoji: '🥕', color: '#ff8c42', trained: false },
    { name: 'Broccoli', emoji: '🥦', color: '#51cf66', trained: false },
    { name: 'Cucumber', emoji: '🥒', color: '#69db7c', trained: false },
    { name: 'Bell Pepper', emoji: '🫑', color: '#94d82d', trained: false },
    { name: 'Eggplant', emoji: '🍆', color: '#9775fa', trained: false },
    { name: 'Cabbage', emoji: '🥬', color: '#8ce99a', trained: false },
    { name: 'Corn', emoji: '🌽', color: '#ffd43b', trained: false },
    { name: 'Mushroom', emoji: '🍄', color: '#f1f3f5', trained: false },
    { name: 'Garlic', emoji: '🧄', color: '#f8f9fa', trained: false }
];

const VegetablesShowcase = () => {
    return (
        <div className="page-container">
            <div className="showcase-section">
                <h1 className="showcase-title">Fresh Vegetables Classification</h1>
                <p className="showcase-subtitle">
                    AI-powered recognition for India's freshest produce
                </p>

                <div className="vegetables-grid">
                    {vegetables.map((veg, index) => (
                        <div
                            key={index}
                            className={`vegetable-card ${veg.trained ? 'trained' : 'coming-soon'}`}
                            style={{ '--veg-color': veg.color }}
                        >
                            <div className="veg-emoji">{veg.emoji}</div>
                            <h3 className="veg-name">{veg.name}</h3>
                            {veg.trained ? (
                                <span className="veg-badge trained-badge">✓ AI Ready</span>
                            ) : (
                                <span className="veg-badge soon-badge">Coming Soon</span>
                            )}
                        </div>
                    ))}
                </div>

                <div className="cta-section">
                    <h2>Try Our AI Classifier</h2>
                    <p>Currently supporting Tomato, Potato, Onion, and Indian Market classification</p>
                    <Link to="/classifier" className="cta-button-large">
                        Start Classifying →
                    </Link>
                </div>

                <div className="stats-section">
                    <div className="stat-card">
                        <div className="stat-number">5</div>
                        <div className="stat-label">AI Models</div>
                    </div>
                    <div className="stat-card">
                        <div className="stat-number">3,135</div>
                        <div className="stat-label">Training Images</div>
                    </div>
                    <div className="stat-card">
                        <div className="stat-number">93%+</div>
                        <div className="stat-label">Accuracy</div>
                    </div>
                    <div className="stat-card">
                        <div className="stat-number">&lt;1s</div>
                        <div className="stat-label">Prediction Time</div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default VegetablesShowcase;
