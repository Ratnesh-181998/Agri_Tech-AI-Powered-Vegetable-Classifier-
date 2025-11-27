@echo off
echo Starting Ninjacart CV Classification Web App...

echo Starting Backend...
start cmd /k "cd backend && pip install -r requirements.txt && python run.py"

echo Starting Frontend...
start cmd /k "cd frontend && npm install && npm run dev"

echo.
echo ===================================================
echo App is starting!
echo Backend will be at: http://localhost:8000
echo Frontend will be at: http://localhost:5173
echo.
echo Note: If this is the first run, the backend will need to train the models.
echo You can manually run 'python backend/train_models.py' to train them.
echo ===================================================
pause
