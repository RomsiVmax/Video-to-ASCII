#When converting to json with third party tools, recommended width for this renderer is 209 and recommended aspect ratio is 2.1

from pathlib import Path
from winsound import PlaySound, SND_FILENAME, SND_ASYNC
from threading import Thread
import json
import time

with open(f"{Path(__file__).resolve().parents[1]}/ascii.json", 'r', encoding='utf-8') as file:
    ascii = json.load(file, strict=False)



frames = ascii["frames"]
frameCount = ascii["frameCount"]
frameRate = ascii["frameRate"]
print(f"[DEBUG] Initialising video with: frameRate {frameRate}, frameCount {frameCount}")
time.sleep(3)


print(f"{Path(__file__).resolve().parents[1]}/sound.wav")
audio_thread = Thread(target=lambda: PlaySound(f"{Path(__file__).resolve().parents[1]}/sound.wav", SND_FILENAME | SND_ASYNC))
audio_thread.start()

for i in range(frameCount):

    rows = frames[i]["rows"]
    for i in range(len(rows)):

        row = rows[i]
        print(row)

    time.sleep(1 / frameRate)
        