import cv2
from pathlib import Path
from os import listdir
from sys import stdout


with open(f"{Path(__file__).resolve().parents[1]}/outputs/grayscale_values.json", "w") as file:

    file.write("{\n")
    file.write("  \"format\": \"grayscale-video-frames\",\n")

    file.write("  \"frames\": [\n")

    frame_files = len([f for f in listdir(f"{Path(__file__).resolve().parents[1]}/outputs/frames/")])
    frame_file_count = 0
    for frame_file in range(frame_files):
        stdout.write(f"\rFrameiplier - Processing frame {frame_file_count} of {frame_files-1}")
        frame_file_count = frame_file_count + 1
        img = cv2.imread(f"{Path(__file__).resolve().parents[1]}/outputs/frames/frame{frame_file+1}.png", 0)

        file.write("    {\n")
        file.write("      \"rows\": [\n")

        row_count = -1
        for row in range (img.shape[0]):
            row_count = row_count+1

        for row in range (img.shape[0]):
            file.write("        \"")
            for pixel_in_row in range (img.shape[1]):
                file.write(f"{str(img[row, pixel_in_row])}, ")
            file.write("\"")
            if row != row_count:
                file.write(",")
            file.write("\n")

        file.write("      ]\n")
        file.write("    }")
        if frame_file_count != frame_files:
            file.write(",")
        file.write("\n")


    file.write("  ]\n")
    file.write("}")

    print()


            