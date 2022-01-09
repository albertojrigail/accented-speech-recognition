#! /usr/bin/env python3.
# Client for interacting with Mozilla Deep Speech.
# Adapted from https://scgupta.medium.com/how-to-build-python-transcriber-using-mozilla-deepspeech-5485b8d234cf.
import subprocess
from os.path import exists
from custom_filesystem import CustomFilesystem
from constants import DEEPSPEECH_ASR_NAME

class DeepspeechTranscribeClient:
    def __init__(self):
        self._custom_filesystem = CustomFilesystem()
    
    def name(self):
        return DEEPSPEECH_ASR_NAME

    def transcribe_recording(self, recording_path):
        deepspeech_model_path = self._custom_filesystem.deepspeech_model_path()
        deepspeech_scorer_path = self._custom_filesystem.deepspeech_scorer_path()
        cmd = ["deepspeech", "--model", deepspeech_model_path, "--scorer", deepspeech_scorer_path, "--audio", recording_path]
        test = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout = test.communicate()[0]
        transcript = stdout.decode("utf-8")
        return transcript

# Example use case of transcribing a recording using the client.
def test_deepspeech_transcribe():
    custom_filesystem = CustomFilesystem()
    recording_path = custom_filesystem.wav_recording_path("spanish1")
    print(recording_path)

    transcribe_client = DeepspeechTranscribeClient()
    transcription = transcribe_client.transcribe_recording(recording_path)
    print(transcription, end="")

if __name__ == '__main__':
    test_deepspeech_transcribe()