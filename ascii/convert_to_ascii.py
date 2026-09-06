from os import system, mkdir
from shutil import rmtree
from pathlib import Path
from time import sleep

print("Ascii converter (really slow btw)");print();print()
sleep(3)
path = Path(__file__).resolve().parents[0]

print("[DEBUG] Deleting old outputs folder if existent")
if Path.exists(f"{path}/conversion/outputs"):
    rmtree(f"{path}/conversion/outputs")

print("[DEBUG] Recreating output folder with the required subfolders")
mkdir(f"{path}/conversion/outputs")
mkdir(f"{path}/conversion/outputs/frames")

print("[DEBUG] Preperations done, moving onto launching the scripts")

print("[DEBUG] Extracting sound")
system(f"python {path}/conversion/sound/sound.py")

print("[DEBUG] Extracting grayscale video")
system(f"python {path}/conversion/grayscale/grayscale_video.py")

print("[DEBUG] Extracting frames into images")
sleep(3)
system(f"python {path}/conversion/frames/frames.py")

print("[DEBUG] Converting images into the \"grayscale-video-frames\" format")
system(f"python {path}/conversion/grayness_values/grayness_values.py")

print("[DEBUG] Converting from the \"grayscale-video-frames\" format to ASCII")
sleep(3)
system(f"python {path}/conversion/ascii/ascii.py")

print("");print("");print("[DEBUG] Done converting the video into ASCII.");print("[DEBUG] Result saved to /ascii.json.")