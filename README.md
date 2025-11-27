# Ninjacart CV Image Classification

## 📋 Project Overview

This project implements a **Computer Vision Image Classification** solution for Ninjacart, India's largest fresh produce supply chain company. The goal is to develop robust classifiers that can distinguish between images of different types of vegetables (onions, potatoes, tomatoes) while correctly labeling images that do not contain any specific vegetable as noise (Indian market scenes).

## 🎯 Problem Statement

Ninjacart sources fresh produce from farmers and delivers them to businesses within 12 hours. An integral component of their automation process is the development of robust classifiers which can:
- Distinguish between images of different types of vegetables
- Correctly label images that do not contain any one type of vegetable as noise

## 📊 Dataset Information

### Dataset Link
[Google Drive Dataset](https://drive.google.com/file/d/1clZX-lV_MLxKHSyeyTheX5OCQtNCUcqT/view?usp=sharing)

### Dataset Structure

**Training Set (3,135 images):**
- Tomato: 789 images
- Potato: 898 images
- Onion: 849 images
- Indian Market (Noise): 599 images

**Test Set (351 images):**
- Tomato: 106 images
- Potato: 83 images
- Onion: 81 images
- Indian Market (Noise): 81 images

### Data Collection
The images in this dataset were scraped from Google and represent real-world scenarios of vegetable classification.

## 🔬 Concepts Tested

1. **Dataset Preparation & Visualization**
2. **CNN Models (Convolutional Neural Networks)**
3. **Implementing Callbacks**
4. **Dealing with Overfitting**
5. **Transfer Learning**

## 🛠️ Technical Implementation

### Libraries Used
- TensorFlow/Keras
- Matplotlib
- OpenCV
- Seaborn
- NumPy
- Pandas

### Model Architecture

The project implements multiple approaches:

1. **Custom CNN from Scratch**
   - Baseline CNN architecture
   - Improved CNN with regularization techniques

2. **Transfer Learning Models**
   - VGG (Visual Geometry Group)
   - ResNet (Residual Networks)
   - MobileNet

### Key Features

- **Data Augmentation**: Applied to increase dataset diversity
- **Batch Normalization**: For stable training
- **Dropout Layers**: To prevent overfitting
- **Callbacks Implementation**:
  - EarlyStopping
  - ModelCheckpoint
  - TensorBoard

## 📈 Evaluation Criteria (100 Points)

### 1. Data Exploration (10 points)
- Importing dataset
- Checking structure & characteristics
- Exploratory analysis

### 2. Exploratory Data Analysis (20 points)
- Class distribution plotting (10 points)
- Visualizing image dimensions (10 points)

### 3. Data Preparation (10 points)
- Train/Validation/Test split

### 4. Model Training (50 points)
- CNN Classifier from scratch (10 points)
- Improving baseline CNN (10 points)
- Implementing callbacks (10 points)
- Fine-tuning pretrained models (10 points)
- Training metrics and confusion matrix (10 points)

### 5. Model Testing (20 points)
- Testing on test set (10 points)
- Summary & insights (10 points)

## 🚀 Getting Started

### Prerequisites
```bash
pip install tensorflow
pip install keras
pip install matplotlib
pip install opencv-python
pip install seaborn
pip install numpy
pip install pandas
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Ninjacart-CV-Classification.git
cd Ninjacart-CV-Classification
```

2. Download the dataset from the provided Google Drive link

3. Extract the dataset to the `ninjacart_data` folder

4. Run the Jupyter notebook:
```bash
jupyter notebook Ninjacart_CV_Image_classification.ipynb
```

## 📁 Project Structure

```
Ninjacart-CV-Classification/
│
├── ninjacart_data/
│   ├── train/
│   │   ├── tomato/
│   │   ├── potato/
│   │   ├── onion/
│   │   └── indian_market/
│   └── test/
│       ├── tomato/
│       ├── potato/
│       ├── onion/
│       └── indian_market/
│
├── NinjaCart DOC/
│   ├── Ninjacart_Case_Study.pdf
│   ├── Ratnesh_Ninjacart_Case_Study.pdf
│   └── ninjacart-cv-image-classification.pdf
│
├── Ninjacart_CV_Image_classification.ipynb
├── Ninjacart CV Classification.txt
├── README.md
├── .gitignore
└── requirements.txt
```

## 📊 Results

The models were evaluated based on:
- **Accuracy**: Overall classification accuracy
- **Precision**: Class-wise precision
- **Recall**: Class-wise recall
- **F1-Score**: Harmonic mean of precision and recall
- **Confusion Matrix**: Visual representation of predictions

## 🔍 Key Insights

1. **Image Preprocessing**: Proper image resizing and normalization significantly improved model performance
2. **Transfer Learning**: Pre-trained models (VGG, ResNet, MobileNet) showed superior performance compared to custom CNN
3. **Data Augmentation**: Helped in reducing overfitting and improving generalization
4. **Class Imbalance**: Addressed through weighted loss functions and data augmentation

## 🎓 Learning Outcomes

- Understanding of CNN architectures for image classification
- Practical implementation of transfer learning
- Techniques to handle overfitting in deep learning models
- Experience with TensorBoard for model monitoring
- Real-world application of computer vision in supply chain automation

## 👨‍💻 Author

**Ratnesh Kumar**

## 🌐 Web Application

This project now includes a full-stack web application with a React frontend and FastAPI backend.

### Features
- **Modern UI**: Glassmorphism design with smooth animations.
- **Real-time Prediction**: Upload an image and get instant classification.
- **Confidence Score**: See how confident the model is.

### How to Run

1. **One-Click Run (Windows)**:
   Double-click `run_project.bat`. This will start both the backend and frontend servers.

2. **Manual Setup**:

   **Backend**:
   ```bash
   cd backend
   pip install -r requirements.txt
   # Train the model (first time only)
   python train.py
   # Start the server
   python main.py
   ```

   **Frontend**:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

3. Open your browser at `http://localhost:5173`

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Ninjacart for providing the business case study
- The deep learning community for pre-trained models
- Google for the dataset hosting platform

## 📧 Contact

For any queries or suggestions, please reach out through:
- GitHub Issues
- Email: [Your Email]

---

**Note**: This project was developed as part of a computer vision case study for Ninjacart's vegetable classification automation system.
