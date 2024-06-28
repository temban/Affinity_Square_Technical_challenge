@echo off
:: Navigate to the backend directory
cd Backend

:: Install Python dependencies
pip install -r requirements.txt

:: Run the server
python main.py
