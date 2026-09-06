import moviepy as mp
from pathlib import Path

video = mp.VideoFileClip(f"{Path(__file__).resolve().parents[2]}/source.mp4")
video.audio.write_audiofile(f"{Path(__file__).resolve().parents[1]}/outputs/sound.mp3")