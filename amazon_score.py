#! /usr/bin/env python3.
# Using the Amazon Transcribe ASR, get the transcriptions for all recordings in the Speech Accent Archive Dataset, and
# calculate the WER score for these transcriptions aggregating scores by the speaker's foreign language.
from wer import WER
import speech_accent_archive_analysis 
from amazon_transcribe_client import AmazonTranscribeClient
from amazon_bucket_client import AmazonBucketClient

recordings_per_language = speech_accent_archive_analysis.recordings_per_language()

wer = WER()
amazon_transcribe_client = AmazonTranscribeClient()
asr_name = amazon_transcribe_client.name()
transcribe_recording = amazon_transcribe_client.transcribe_recording
recording_path = AmazonBucketClient().mp3_recording_path

score_per_language = wer.score_asr_per_language(asr_name, recordings_per_language, transcribe_recording, recording_path)