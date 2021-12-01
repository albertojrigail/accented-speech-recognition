#! /usr/bin/env python3.
# Client for interacting with the Google Speech-to-text API.
# Adapted from https://gist.github.com/gxercavins/a4deaf7f0efa5c4f23e1f3b59088eb72.
import os
import io
from google.cloud import speech_v1p1beta1
from google.cloud.speech_v1p1beta1 import types
from custom_filesystem import CustomFilesystem
from constants import GOOGLE_ASR_NAME

class GoogleTranscribeClient:
    def __init__(self):
        custom_filesystem = CustomFilesystem()
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = custom_filesystem.google_auth_path()
        self._client = speech_v1p1beta1.SpeechClient()

    def name(self):
        return GOOGLE_ASR_NAME

    def transcribe_recording(self, recording_path):
        with io.open(recording_path, 'rb') as audio_file:
            content = audio_file.read()
        stream = [content]
        requests = (types.StreamingRecognizeRequest(audio_content=chunk)
                    for chunk in stream)
        config = types.RecognitionConfig(
            encoding=types.RecognitionConfig.AudioEncoding.MP3,
            sample_rate_hertz=16000,
            language_code='en-US')
        streaming_config = types.StreamingRecognitionConfig(config=config)
        responses = self._client.streaming_recognize(streaming_config, requests)
        transcript = ""
        for response in responses:
            for result in response.results:
                alternatives = result.alternatives
                if len(alternatives) > 0:
                    alternative = alternatives[0]
                    transcript = transcript + alternative.transcript
        return transcript

# Example use case of transcribing a recording using the client.
def test_google_transcribe():
    custom_filesystem = CustomFilesystem()
    recording_path = custom_filesystem.mp3_recording_path("english1")
    print(recording_path)

    transcribe_client = GoogleTranscribeClient()
    transcription = transcribe_client.transcribe_recording(recording_path)
    print(transcription)

if __name__ == '__main__':
    test_google_transcribe()