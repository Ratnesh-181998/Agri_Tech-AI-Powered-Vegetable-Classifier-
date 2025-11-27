import React, { useEffect, useState } from 'react';

const PredictionResult = ({ prediction, error }) => {
    const [width, setWidth] = useState(0);

    useEffect(() => {
        if (prediction) {
            // Small delay to trigger animation
            const timer = setTimeout(() => {
                setWidth(prediction.confidence * 100);
            }, 100);
            return () => clearTimeout(timer);
        } else {
            setWidth(0);
        }
    }, [prediction]);

    if (error) {
        return <div className="error-message">{error}</div>;
    }

    if (!prediction) return null;

    return (
        <div className="result-section">
            <h2>Analysis Result</h2>
            <div className="result-card">
                <span className="class-name">{prediction.class}</span>
                <div className="confidence-bar">
                    <div
                        className="confidence-fill"
                        style={{ width: `${width}%` }}
                    ></div>
                </div>
                <span className="confidence-text">
                    {(prediction.confidence * 100).toFixed(1)}% Confidence Score
                </span>
            </div>
            {prediction.message && <p className="info-text">{prediction.message}</p>}
        </div>
    );
};

export default PredictionResult;
