#! /usr/bin/env python3.
# Using the Mozilla Deep Speech ASR, get the transcriptions for all recordings in the Speech Accent Archive Dataset, and
# calculate the WER score for these transcriptions aggregating scores by the speaker's foreign language.
from wer import WER
import speech_accent_archive_analysis
from deepspeech_transcribe_client import DeepspeechTranscribeClient
from custom_filesystem import CustomFilesystem

recordings_per_language = speech_accent_archive_analysis.recordings_per_language()

wer = WER()
deepspeech_transcribe_client = DeepspeechTranscribeClient()
asr_name = deepspeech_transcribe_client.name()
transcribe_recording = deepspeech_transcribe_client.transcribe_recording
recording_path = CustomFilesystem().wav_recording_path

score_per_language = wer.score_asr_per_language(asr_name, recordings_per_language, transcribe_recording, recording_path)