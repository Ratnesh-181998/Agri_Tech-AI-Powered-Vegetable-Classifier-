import React, { useState } from 'react';

const ImageUploader = ({ preview, onFileChange }) => {
    const [isDragging, setIsDragging] = useState(false);

    const handleDragOver = (e) => {
        e.preventDefault();
        setIsDragging(true);
    };

    const handleDragLeave = () => {
        setIsDragging(false);
    };

    const handleDrop = (e) => {
        e.preventDefault();
        setIsDragging(false);
        const files = e.dataTransfer.files;
        if (files && files.length > 0) {
            // Create a fake event object to reuse the onFileChange handler
            onFileChange({ target: { files: files } });
        }
    };

    return (
        <div className="upload-section">
            <input
                type="file"
                id="file-upload"
                accept="image/*"
                onChange={onFileChange}
                hidden
            />
            <label
                htmlFor="file-upload"
                className={`upload-box ${isDragging ? 'drag-active' : ''}`}
                onDragOver={handleDragOver}
                onDragLeave={handleDragLeave}
                onDrop={handleDrop}
            >
                {preview ? (
                    <img src={preview} alt="Preview" className="image-preview" />
                ) : (
                    <div className="placeholder">
                        <span className="icon">📁</span>
                        <p>Drag & Drop or Click to Upload</p>
                    </div>
                )}
            </label>
        </div>
    );
};

export default ImageUploader;
