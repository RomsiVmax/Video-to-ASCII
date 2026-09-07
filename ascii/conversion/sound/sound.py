from lib.audio.portaudio import extract_audio
from pathlib import Path

extract_audio(input_path=f"{Path(__file__).resolve().parents[2]}/source.mp4", output_path=f"{Path(__file__).resolve().parents[2]}/sound.wav")