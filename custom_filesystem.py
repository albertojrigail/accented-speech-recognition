#! /usr/bin/env python3.
import os
from constants import TOP_LEVEL_DIR, DATA_DIR, RECORDINGS_DIR, DEEPSPEECH_DIR, GOOGLE_DIR, ASR_SCORES_DIR
from constants import SPEAKERS_FILE, PASSAGE_FILE, DEEPSPEECH_MODEL_FILE, DEEPSPEECH_SCORER_FILE, GOOGLE_AUTH_FILE
from constants import MP3_EXTENSION, WAV_EXTENSION
from constants import AMAZON_ACCESS_KEY_ID, AMAZON_SECRET_ACCESS_KEY, AMAZON_BUCKET_NAME

class CustomFilesystem:
    def speakers_file_path(self):
        return os.path.join(TOP_LEVEL_DIR, DATA_DIR, SPEAKERS_FILE)

    def passage_path(self):
        return os.path.join(TOP_LEVEL_DIR, DATA_DIR, PASSAGE_FILE)

    def _recording_path(self, file_without_extension, extension):
        return os.path.join(TOP_LEVEL_DIR, DATA_DIR, RECORDINGS_DIR, file_without_extension) + extension

    def mp3_recording_path(self, file_without_extension):
        return self._recording_path(file_without_extension, MP3_EXTENSION)
    
    def wav_recording_path(self, file_without_extension):
        return self._recording_path(file_without_extension, WAV_EXTENSION)

    def google_auth_path(self):
        return os.path.join(TOP_LEVEL_DIR, GOOGLE_DIR, GOOGLE_AUTH_FILE)

    def deepspeech_model_path(self):
        return os.path.join(TOP_LEVEL_DIR, DEEPSPEECH_DIR, DEEPSPEECH_MODEL_FILE)

    def deepspeech_scorer_path(self):
        return os.path.join(TOP_LEVEL_DIR, DEEPSPEECH_DIR, DEEPSPEECH_SCORER_FILE)

    def asr_score_path(self, score_file):
        return os.path.join(TOP_LEVEL_DIR, ASR_SCORES_DIR, score_file)
