@echo off
echo Installing dependencies if not already installed
pip install moviepy
pip install opencv-python
pip install mutagen
cls
python internal/convert_to_ascii.py
pause>nul