# Ninjacart CV Image Classification

## 📋 Project Overview

This project implements a **Computer Vision Image Classification** solution for Ninjacart, India's largest fresh produce supply chain company. The goal is to develop robust classifiers that can distinguish between images of different types of vegetables (onions, potatoes, tomatoes) while correctly labeling images that do not contain any specific vegetable as noise (Indian market scenes).

## 🎯 Problem Statement

Ninjacart sources fresh produce from farmers and delivers them to businesses within 12 hours. An integral component of their automation process is the development of robust classifiers which can:
- Distinguish between images of different types of vegetables
- Correctly label images that do not contain any one type of vegetable as noise

  <img width="838" height="1240" alt="image" src="https://github.com/user-attachments/assets/75125a96-a062-420f-8b2c-72d3c6c6906a" />

  <img width="1276" height="1307" alt="image" src="https://github.com/user-attachments/assets/b2c40c2c-da12-4928-9c44-452ada8eead7" />

  <img width="695" height="1275" alt="image" src="https://github.com/user-attachments/assets/4f1614b4-5964-4d6c-814d-61392599b268" />
  <img width="675" height="1273" alt="image" src="https://github.com/user-attachments/assets/9c4e0498-9b78-45df-a304-33e09aac9e93" />
 <img width="693" height="1275" alt="image" src="https://github.com/user-attachments/assets/497eb882-8dbc-4ef5-8802-40ad7ecd7443" />
<img width="678" height="1277" alt="image" src="https://github.com/user-attachments/assets/3a8b9b81-9f2e-4b99-a844-247a76b42e99" />
<img width="1347" height="1503" alt="image" src="https://github.com/user-attachments/assets/04afcf8e-7c4d-49c6-aa1e-95ca9774fb0a" />


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

<img width="2873" height="1697" alt="image" src="https://github.com/user-attachments/assets/4ac5518b-e6df-4605-b918-969475e9155b" />

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
- GitHub Issues - https://github.com/Ratnesh-181998
- Linkedin- https://www.linkedin.com/in/ratneshkumar1998/
- Email:rattudacsit2021gate@gmail.com

---

**Note**: This project was developed as part of a computer vision case study for Ninjacart's vegetable classification automation system.


---


<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=24,20,12,6&height=3" width="100%">


## 📜 **License**

![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge&logo=opensourceinitiative&logoColor=white)

**Licensed under the MIT License** - Feel free to fork and build upon this innovation! 🚀

---

# 📞 **CONTACT & NETWORKING** 📞


### 💼 Professional Networks

[![LinkedIn](https://img.shields.io/badge/💼_LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ratneshkumar1998/)
[![GitHub](https://img.shields.io/badge/🐙_GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Ratnesh-181998)
[![X](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/RatneshS16497)
[![Portfolio](https://img.shields.io/badge/🌐_Portfolio-FF6B6B?style=for-the-badge&logo=google-chrome&logoColor=white)](https://share.streamlit.io/user/ratnesh-181998)
[![Email](https://img.shields.io/badge/✉️_Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:rattudacsit2021gate@gmail.com)
[![Medium](https://img.shields.io/badge/Medium-000000?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@rattudacsit2021gate)
[![Stack Overflow](https://img.shields.io/badge/Stack_Overflow-F58025?style=for-the-badge&logo=stack-overflow&logoColor=white)](https://stackoverflow.com/users/32068937/ratnesh-kumar)

### 🚀 AI/ML & Data Science
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://share.streamlit.io/user/ratnesh-181998)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/RattuDa98)
[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/rattuda)

### 💻 Competitive Programming (Including all coding plateform's 5000+ Problems/Questions solved )
[![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/Ratnesh_1998/)
[![HackerRank](https://img.shields.io/badge/HackerRank-00EA64?style=for-the-badge&logo=hackerrank&logoColor=black)](https://www.hackerrank.com/profile/rattudacsit20211)
[![CodeChef](https://img.shields.io/badge/CodeChef-5B4638?style=for-the-badge&logo=codechef&logoColor=white)](https://www.codechef.com/users/ratnesh_181998)
[![Codeforces](https://img.shields.io/badge/Codeforces-1F8ACB?style=for-the-badge&logo=codeforces&logoColor=white)](https://codeforces.com/profile/Ratnesh_181998)
[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-2F8D46?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/profile/ratnesh1998)
[![HackerEarth](https://img.shields.io/badge/HackerEarth-323754?style=for-the-badge&logo=hackerearth&logoColor=white)](https://www.hackerearth.com/@ratnesh138/)
[![InterviewBit](https://img.shields.io/badge/InterviewBit-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://www.interviewbit.com/profile/rattudacsit2021gate_d9a25bc44230/)


---

## 📊 **GitHub Stats & Metrics** 📊



![Profile Views](https://komarev.com/ghpvc/?username=Ratnesh-181998&color=blueviolet&style=for-the-badge&label=PROFILE+VIEWS)




<img 
  src="https://streak-stats.demolab.com?user=Ratnesh-181998&theme=radical&hide_border=true&background=0D1117&stroke=4ECDC4&ring=F38181&fire=FF6B6B&currStreakLabel=4ECDC4"
  alt="GitHub Streak Stats"
width="48%"/>




<img src="https://github-readme-activity-graph.vercel.app/graph?username=Ratnesh-181998&theme=react-dark&hide_border=true&bg_color=0D1117&color=4ECDC4&line=F38181&point=FF6B6B" width="48%" />

---

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=24&duration=3000&pause=1000&color=4ECDC4&center=true&vCenter=true&width=600&lines=Ratnesh+Kumar+Singh;Data+Scientist+%7C+AI%2FML+Engineer;4%2B+Years+Building+Production+AI+Systems" alt="Typing SVG" />

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=18&duration=2000&pause=1000&color=F38181&center=true&vCenter=true&width=600&lines=Built+with+passion+for+the+AI+Community+🚀;Innovating+the+Future+of+AI+%26+ML;MLOps+%7C+LLMOps+%7C+AIOps+%7C+GenAI+%7C+AgenticAI+Excellence" alt="Footer Typing SVG" />


<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer" width="100%">

