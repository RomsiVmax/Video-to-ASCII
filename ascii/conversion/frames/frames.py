from moviepy import VideoFileClip
from pathlib import Path
from math import ceil
from sys import stdout


clip = VideoFileClip(f"{Path(__file__).resolve().parents[1]}/outputs/grayscale_video.mp4")



frame_count=ceil(clip.fps * clip.duration)
processed_frame_count=0





for frame in range((frame_count-2)):
    processed_frame_count=processed_frame_count+1
    stdout.write(f"\rFrameiplier - Processing frame {processed_frame_count} of {frame_count}")
    stdout.flush()
    clip.save_frame(f"{Path(__file__).resolve().parents[1]}/outputs/frames/frame{processed_frame_count}.png", t = (processed_frame_count / clip.fps))
clip.close()


stdout.write(f"\rFrameiplier - Processing frame {processed_frame_count+1} of {frame_count-1}")
stdout.flush()
stdout.flush()
print()

