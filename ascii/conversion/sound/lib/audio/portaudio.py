#!/usr/bin/env python

import argparse


# Other modules
import subprocess
import imageio_ffmpeg

# Local modules
import re
import os



import mutagen


def media_duration(file_path: str):
    file = mutagen.File(file_path)
    duration = file.info.length
    return duration


def seconds_to_hms(seconds: float | int) -> str:
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    hms = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
    return hms


def hms_to_seconds(time_str: str) -> float:
    # Split the time string into hours, minutes, and seconds
    time_parts = time_str.split(':')
    if len(time_parts) == 3:  # HH:MM:SS format
        hours, minutes, seconds = map(int, time_parts)
    elif len(time_parts) == 2:  # MM:SS format
        hours = 0
        minutes, seconds = map(int, time_parts)
    else:
        raise Exception("Invalid time format. Must be in HH:MM:SS or MM:SS format.")

    # Calculate the total number of seconds
    total_seconds = hours * 3600 + minutes * 60 + seconds

    # Return the total number of seconds as a float
    return float(total_seconds)









SUPPORTED_AUDIO_FORMATS = [
    'wav'
]

SUPPORTED_VIDEO_FORMATS = [
    'mp4'
]

SUPPORTED_FFMPEG_FORMATS = SUPPORTED_AUDIO_FORMATS + SUPPORTED_VIDEO_FORMATS


class AudioExtractValidator:

    def __init__(self, input_path: str, output_path: str, output_format: str, duration: float, start_time: str,
                 overwrite: bool):
        self.input_path = input_path
        self.output_path = output_path
        self.output_format = output_format
        self.duration = duration
        self.start_time = start_time
        self.overwrite = overwrite

    def validate(self) -> dict:
        # Validate and clean all inputs
        self._validate_input_path()
        self._validate_output_format()
        self._validate_output_path()
        self._validate_start_time()
        self._validate_duration()
        # Return cleaned and validated inputs
        return self.__dict__

    def _validate_input_path(self):
        input_path = os.path.abspath(self.input_path)

        if not any(input_path.endswith("." + x) for x in SUPPORTED_FFMPEG_FORMATS):
            raise Exception(f"Input file format not supported. Only (Video/Audio) allowed.")

        if not os.path.isfile(input_path):
            raise Exception(f"{input_path} was not found, please provide a valid file path.")

        self.input_path = input_path

    def _validate_output_path(self):
        output_path = self.output_path
        if output_path.endswith("/") or output_path.endswith("\\"):
            output_path += "audio." + self.output_format

        output_path = os.path.abspath(output_path)
        output_parts = output_path.split(os.sep)
        filename = output_parts[-1]
        folder_path = f"{os.sep}".join(output_parts[:-1])

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        extension = "." + self.output_format
        if not filename.endswith(extension):
            output_path = output_path + extension

        if os.path.isfile(output_path) and not self.overwrite:
            raise Exception(f"File already exists in output path: {output_path}.")

        self.output_path = output_path

    def _validate_output_format(self):
        output_format = self.output_format
        if output_format not in SUPPORTED_AUDIO_FORMATS:
            supported_formats = ', '.join(SUPPORTED_AUDIO_FORMATS)
            raise Exception(f"Output format {self.output_format} not supported, Only ({supported_formats}) are supported")

    def _validate_start_time(self):
        start_time = self.start_time

        if start_time == "00:00:00":
            return

        pattern = r"^(?:(\d{1,2}):)?(\d{1,2}):(\d{1,2})$"
        if not re.match(pattern, start_time):
            raise Exception("Invalid time format. Must be in HH:MM:SS or MM:SS format.")

        file_duration = media_duration(self.input_path)
        start_time_seconds = hms_to_seconds(self.start_time)
        if start_time_seconds > file_duration:
            raise Exception("Start time can't be longer than the input (Video/Audio) file duration")

        self.start_time = start_time

    def _validate_duration(self):
        if not self.duration:
            return

        duration = self.duration
        self.duration = str(duration)













FFMPEG_BINARY = imageio_ffmpeg.get_ffmpeg_exe()


def extract_audio(input_path: str, output_path: str = "./audio.wav", output_format: str = "wav",
                  start_time: str = "00:00:00",
                  duration: float = None,
                  overwrite: bool = False):
    validator = AudioExtractValidator(input_path, output_path, output_format, duration, start_time, overwrite)
    result = validator.validate()

    cleaned_input_path = result["input_path"]
    cleaned_output_path = result["output_path"]
    cleaned_output_format = result["output_format"]
    cleaned_start_time = result["start_time"]
    cleaned_duration = result["duration"]

    command = [FFMPEG_BINARY,
               '-i', cleaned_input_path,
               '-ss', cleaned_start_time,
               '-f', cleaned_output_format,
               '-y', cleaned_output_path]

    if cleaned_duration:
        command.insert(3, "-t")
        command.insert(4, cleaned_duration)

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print(f"portaudio - Success : audio file has been saved to \"{cleaned_output_path}\".")