import React, { useState, useEffect } from 'react';
import { getModels } from '../services/api';

const AnalyticsDashboard = ({ selectedModel }) => {
    const [metrics, setMetrics] = useState(null);
    const [plotUrl, setPlotUrl] = useState(null);

    useEffect(() => {
        const fetchAnalytics = async () => {
            try {
                const modelsData = await getModels();
                if (modelsData && modelsData[selectedModel]) {
                    setMetrics(modelsData[selectedModel]);
                }
                setPlotUrl(`http://localhost:8000/analytics/${selectedModel}/plot`);
            } catch (error) {
                console.error("Failed to fetch analytics", error);
            }
        };

        if (selectedModel) {
            fetchAnalytics();
        }
    }, [selectedModel]);

    if (!metrics) return null;

    return (
        <div className="analytics-section">
            <h3>📊 Model Analytics: {selectedModel.toUpperCase()}</h3>

            <div className="metrics-grid">
                <div className="metric-card">
                    <span className="label">Test Accuracy</span>
                    <span className="value">{(metrics.accuracy * 100).toFixed(2)}%</span>
                </div>
                <div className="metric-card">
                    <span className="label">Test Loss</span>
                    <span className="value">{metrics.loss.toFixed(4)}</span>
                </div>
            </div>

            <div className="plot-container">
                <h4>Training History</h4>
                <img
                    src={plotUrl}
                    alt={`${selectedModel} training plot`}
                    onError={(e) => e.target.style.display = 'none'}
                />
            </div>
        </div>
    );
};

export default AnalyticsDashboard;
