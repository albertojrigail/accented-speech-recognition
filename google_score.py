#! /usr/bin/env python3.
# Using the Google Speech-to-text ASR, get the transcriptions for all recordings in the Speech Accent Archive Dataset, and
# calculate the WER score for these transcriptions aggregating scores by the speaker's foreign language.
from wer import WER
import speech_accent_archive_analysis
from google_transcribe_client import GoogleTranscribeClient
from custom_filesystem import CustomFilesystem

recordings_per_language = speech_accent_archive_analysis.recordings_per_language()

wer = WER()
google_transcribe_client = GoogleTranscribeClient()
asr_name = google_transcribe_client.name()
transcribe_recording = google_transcribe_client.transcribe_recording
recording_path = CustomFilesystem().mp3_recording_path

score_per_language = wer.score_asr_per_language(asr_name, recordings_per_language, transcribe_recording, recording_path)