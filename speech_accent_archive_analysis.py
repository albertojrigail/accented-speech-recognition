#! /usr/bin/env python3.
import csv
from os.path import exists
from custom_filesystem import CustomFilesystem
import matplotlib.pyplot as plt


# Split data by native langage using speakers_all.csv.
# Make a map string:list that maps a language to a list of recordings.
def recordings_per_language():
    recordings_dict = {}
    custom_filesystem = CustomFilesystem()
    speakers_file_path = custom_filesystem.speakers_file_path()
    with open(speakers_file_path) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            recording = row[3]
            language = row[4]
            file_missing_default = (row[8] == "TRUE")
            if file_missing_default:
                continue
            file_path = custom_filesystem.mp3_recording_path(recording)
            file_exists = exists(file_path)
            if not file_exists:
                continue
            recordings = recordings_dict.setdefault(language, [])
            recordings.append(recording)
            recordings_dict[language] = recordings
    return recordings_dict

# Show a graph with the number of recordings for each foreign accent (> 30 only).
# Adapted from https://www.geeksforgeeks.org/bar-plot-in-matplotlib/.
def recordings_per_language_graph():
    MIN_RECORDINGS_COUNT = 30
    recordings_dict = recordings_per_language()
    frequency = {}
    for language in recordings_dict:
        count = len(recordings_dict[language])
        if count >= MIN_RECORDINGS_COUNT:
            frequency[language] = count
    fig = plt.figure(figsize = (10, 5))
    plt.bar(frequency.keys(), frequency.values(), color ='maroon', width = 0.4)
    plt.xlabel("Foreign Accent")
    plt.ylabel("Recordings")
    title = "Recording Count Per Accent in the Speech Accent Archive Dataset" + \
    "\n (only accents with >30 recordings)\n"
    plt.title(title)
    return plt

if __name__ == '__main__':
    plt = recordings_per_language_graph()
    plt.show()
