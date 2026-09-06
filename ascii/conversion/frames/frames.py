from moviepy import VideoFileClip
from pathlib import Path
from math import ceil


clip = VideoFileClip(f"{Path(__file__).resolve().parents[1]}/outputs/grayscale_video.mp4")



frame_count=ceil(clip.fps * clip.duration)
processed_frame_count=0


for frame in clip.iter_frames(fps=clip.fps, dtype="uint8"):
    processed_frame_count=processed_frame_count+1
    print(f"Processing frame {processed_frame_count} of {frame_count}")
    clip.save_frame(f"{Path(__file__).resolve().parents[1]}/outputs/frames/frame{processed_frame_count}.png", t = (processed_frame_count / clip.fps))
clip.close()


print(f"Processing frame {processed_frame_count+1} of {frame_count}")
print("Processed all frames.")

