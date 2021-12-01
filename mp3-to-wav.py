#! /usr/bin/env python3.
from os import path
from pydub import AudioSegment
from custom_filesystem import CustomFilesystem, WAV_EXTENSION
import speech_accent_archive_analysis

# Create a wav duplicate (in the same directory) for an mp3 recording.
def create_wav_duplicate(mp3_recording_path):
    path_without_extension = mp3_recording_path[:-4]
    wav_recording_path = path_without_extension + WAV_EXTENSION
    sound = AudioSegment.from_mp3(mp3_recording_path)
    sound.export(wav_recording_path, format="wav")

if __name__ == '__main__':
    # Create wav duplicates for all the recordings in the Speech Accent Archive dataset.
    recordings_per_language = speech_accent_archive_analysis.recordings_per_language()
    custom_filesystem = CustomFilesystem()
    print("Creating wav duplicates for the following files:")
    for language, recordings in recordings_per_language.items():
        for recording in recordings:
            mp3_recording_path = custom_filesystem.mp3_recording_path(recording)
            print(mp3_recording_path)
            create_wav_duplicate(mp3_recording_path)

            