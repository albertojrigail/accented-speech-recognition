#! /usr/bin/env python3.
import string
import re
import time
import csv
import jiwer
from custom_filesystem import CustomFilesystem

class WER:
    def __init__(self):
        self._custom_filesystem = CustomFilesystem()

    def _speech_accent_archive_transcript(self):
        passage_path = self._custom_filesystem.passage_path()
        with open(passage_path, "r") as passage:
            transcript = passage.read()
        return transcript

    # Preprocess string by removing punctuation, digits, extra spaces, and making the string lowercase.
    def _preprocess_string(self, s):
        exclist = string.punctuation + string.digits
        table_ = str.maketrans('', '', exclist)
        s = s.translate(table_)
        s = s.lower()
        s = re.sub(' +', ' ', s)
        return s

    # Compute WER score after preprocessing ground_truth and hypothesis.
    def compute(self, ground_truth, hypothesis):
        ground_truth_preprocessed = self._preprocess_string(ground_truth)
        hypothesis_preprocessed = self._preprocess_string(hypothesis)
        score = jiwer.wer([ground_truth_preprocessed], [hypothesis_preprocessed])
        return score
    
    # Compute an ASR's score per language, and record results to a csv file.
    def score_asr_per_language(self, asr_name, recordings_per_language, transcribe_streaming, recording_path_function):
        print("Scoring " + asr_name)

        # Create csv file.
        asr_file_path = self._custom_filesystem.asr_score_path(asr_name)
        number = 1
        csv_columns = ['number', 'language','score']
        with open(asr_file_path, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()

        # Compute score for all recordings, per language.
        ground_truth = self._speech_accent_archive_transcript()
        score_per_language = {}
        for language, recordings in recordings_per_language.items():
            frequency = len(recordings)
            if frequency == 0:
                continue
            score_sum = 0
            for recording in recordings:
                recording_path = recording_path_function(recording)
                hypothesis = transcribe_streaming(recording_path)
                if hypothesis == "":
                    raise Exception("Failed to transcribe recording")
                score = self.compute(ground_truth, hypothesis)
                score_sum = score_sum + score
            avg_score = score_sum / frequency
            score_per_language[language] = avg_score

            # Insert entry in csv file.
            data = {
                "number" : number,
                "language" : language,
                "score" : avg_score,
            }
            number = number + 1
            with open(asr_file_path, 'a') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writerow(data)
        return score_per_language