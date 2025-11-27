# Ninjacart CV Classification - Website Guide

## 🌐 Website Structure

### Pages Available:
1. **Home** (`/`) - Ninjacart-style landing page with hero banner
2. **Vegetables** (`/vegetables`) - Showcase of all vegetables (trained and coming soon)
3. **Classifier** (`/classifier`) - AI classification tool
4. **About** (`/about`) - Project information

## 🚀 How to Access

Open your browser and visit: **http://localhost:5173**

## ✨ Features

### Home Page:
- Hero banner with CTA buttons
- Features section (4 key benefits)
- Categories section (available vegetables)
- Stats banner (training data, models, accuracy)
- Final CTA section

### Vegetables Page:
- 12 vegetable cards
- Status badges (AI Ready / Coming Soon)
- Interactive hover effects
- Stats section

### Classifier Page:
- Model selector (5 AI models)
- Drag & drop image upload
- Real-time prediction
- Confidence score display
- Analytics dashboard

### About Page:
- Problem statement
- Dataset information
- AI models overview
- Technical stack

## 🎨 Design

- **Style**: Professional Ninjacart e-commerce design
- **Colors**: Green (#00c853), White, Clean grays
- **Font**: Inter (modern, clean)
- **Responsive**: Works on all devices

## 🔧 Troubleshooting

If the website doesn't load:
1. Check if frontend is running: `npm run dev` in frontend folder
2. Check if backend is running: `python run.py` in backend folder
3. Clear browser cache and refresh

## 📊 Backend Status

- Training: In progress (check with `python check_training.py`)
- API: Running on http://localhost:8000
- Models: Saved in `backend/saved_models/`
