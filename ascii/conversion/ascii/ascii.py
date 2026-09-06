import json
from pathlib import Path
import re
from sys import stdout

with open(f"{Path(__file__).resolve().parents[1]}/outputs/grayscale_values.json", "r") as file:
    grayness_values = json.load(file, strict=False)

    frames = grayness_values["frames"]
    frameCount= len(frames)



    with open(f"{Path(__file__).resolve().parents[2]}/ascii.json", 'a', encoding='utf-8') as ascii_file:
        ascii_file.write(f"  \"frameCount\": {frameCount},\n")
        ascii_file.write("  \"frames\": [\n")

        
    current_frame = 0
    for i in range(frameCount): #frames
        current_frame = current_frame + 1

        with open(f"{Path(__file__).resolve().parents[2]}/ascii.json", 'a', encoding='utf-8') as ascii_file:
            ascii_file.write("    {\n")
            ascii_file.write("      \"rows\": [\n")


        rows = frames[i]["rows"]
        rows_count = len(rows)
        current_row = 0
        for row in range(len(rows)): #rows
            
            row = rows[row]

            row = re.findall('[0-9]+', row)
            ascii_row=""
            for number in row: #row
                if int(number) <= 32:
                    ascii_row = f"{ascii_row}@"
                elif int(number) <= 64:
                    ascii_row = f"{ascii_row}%"
                elif int(number) <= 96:
                    ascii_row = f"{ascii_row}#"
                elif int(number) <= 128:
                    ascii_row = f"{ascii_row}+"
                elif int(number) <= 160:
                    ascii_row = f"{ascii_row}="
                elif int(number) <= 192:
                    ascii_row = f"{ascii_row}-"
                elif int(number) <= 224:
                    ascii_row = f"{ascii_row}:"
                elif int(number) <= 256:
                    ascii_row = f"{ascii_row}."

            current_row = current_row + 1
            with open(f"{Path(__file__).resolve().parents[2]}/ascii.json", 'a', encoding='utf-8') as ascii_file:
                ascii_file.write(f"        \"{ascii_row}\"")
                if current_row !=  rows_count:
                    ascii_file.write(",")
                ascii_file.write("\n")
                    
        
        with open(f"{Path(__file__).resolve().parents[2]}/ascii.json", 'a', encoding='utf-8') as ascii_file:
            ascii_file.write("      ]\n")
            ascii_file.write("    }")
            stdout.write(f"\rASCII.Remaker - Processing frame {current_frame} of {frameCount} into ASCII")
            stdout.flush()
            if current_frame !=  frameCount:
                ascii_file.write(",")
            ascii_file.write("\n")



    with open(f"{Path(__file__).resolve().parents[2]}/ascii.json", 'a', encoding='utf-8') as ascii_file:
        ascii_file.write(f"  ]\n")
        ascii_file.write("}")
        print("\n")


    
file.close()

