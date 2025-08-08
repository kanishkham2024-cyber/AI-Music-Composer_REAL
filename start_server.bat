@echo off
cd /d "C:\Users\User\ai-music-backend"
call venv\Scripts\activate.bat
uvicorn main:app --reload
pause
