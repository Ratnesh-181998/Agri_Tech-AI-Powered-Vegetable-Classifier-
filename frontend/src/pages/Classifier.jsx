import { useState } from 'react'
import ModelSelector from '../components/ModelSelector'
import ImageUploader from '../components/ImageUploader'
import PredictionResult from '../components/PredictionResult'
import AnalyticsDashboard from '../components/AnalyticsDashboard'
import { predictImage } from '../services/api'

function Classifier() {
    const [file, setFile] = useState(null)
    const [preview, setPreview] = useState(null)
    const [prediction, setPrediction] = useState(null)
    const [loading, setLoading] = useState(false)
    const [error, setError] = useState(null)
    const [selectedModel, setSelectedModel] = useState('mobilenet')

    const handleFileChange = (e) => {
        const selectedFile = e.target.files[0]
        if (selectedFile) {
            setFile(selectedFile)
            setPreview(URL.createObjectURL(selectedFile))
            setPrediction(null)
            setError(null)
        }
    }

    const handlePredict = async () => {
        if (!file) return

        setLoading(true)
        setError(null)

        try {
            const data = await predictImage(file, selectedModel)
            setPrediction(data)
        } catch (err) {
            setError('Failed to get prediction. Ensure backend is running and models are trained.')
        } finally {
            setLoading(false)
        }
    }

    return (
        <div className="classifier-page">
            <div className="classifier-container">
                <div className="classifier-header">
                    <h1>Ninjacart Classifier</h1>
                    <p>AI-Powered Fresh Produce Recognition</p>
                </div>

                <div className="classifier-content">
                    <ModelSelector
                        selectedModel={selectedModel}
                        onSelectModel={setSelectedModel}
                    />

                    <ImageUploader
                        preview={preview}
                        onFileChange={handleFileChange}
                    />

                    <button
                        className="btn btn-primary btn-classify"
                        onClick={handlePredict}
                        disabled={!file || loading}
                    >
                        {loading ? 'Analyzing...' : 'Identify Vegetable'}
                    </button>

                    <PredictionResult
                        prediction={prediction}
                        error={error}
                    />

                    <AnalyticsDashboard selectedModel={selectedModel} />
                </div>
            </div>
        </div>
    )
}

export default Classifier
