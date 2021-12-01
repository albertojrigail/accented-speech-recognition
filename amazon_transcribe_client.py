#! /usr/bin/env python3.
# Client for interacting with the Amazon Transcribe API.
# Adapted from https://medium.com/@iopheam/how-to-start-using-amazon-transcribe-service-with-python-c7fad9c726b5.
import time
import boto3
import urllib.request
import json
from custom_filesystem import AMAZON_ACCESS_KEY_ID, AMAZON_SECRET_ACCESS_KEY
from amazon_bucket_client import AmazonBucketClient
from constants import AMAZON_ASR_NAME

class AmazonTranscribeClient:

    def __init__(self):
        self._client = boto3.client(
            'transcribe',
            aws_access_key_id = AMAZON_ACCESS_KEY_ID,
            aws_secret_access_key = AMAZON_SECRET_ACCESS_KEY,
            region_name = "us-east-1",
        )

    def name(self):
        return AMAZON_ASR_NAME

    # Start an Amazon Transcribe job.
    def _start_transcribe_job(self, amazon_recording_uri, job_name):
        try:
            self._client.start_transcription_job(
                TranscriptionJobName=job_name,
                Media={'MediaFileUri': amazon_recording_uri},
                MediaFormat='mp3',
                LanguageCode='en-US')
            return True
        except Exception as e:
            print(e)
            return None

    def _transcription_text(self, job_name):
        while True:
            job = self._client.get_transcription_job(TranscriptionJobName=job_name)
            status = job['TranscriptionJob']['TranscriptionJobStatus']
            if status == 'COMPLETED':
                with urllib.request.urlopen(job['TranscriptionJob']['Transcript']['TranscriptFileUri']) as r:
                    data = json.loads(r.read())
                return data['results']['transcripts'][0]['transcript']
            elif status == 'FAILED':
                print("Status: FAILED")
                return None
            else:
                time.sleep(5)

    def transcribe_recording(self, amazon_recording_uri):
        job_name = amazon_recording_uri.split("/")[-1]
        job_status = self._start_transcribe_job(amazon_recording_uri, job_name)
        if not job_status:
            return ""
        transcription = self._transcription_text(job_name)
        if not transcription:
            return ""
        return transcription
    
    def _transcription_jobs(self):
        response = self._client.list_transcription_jobs(MaxResults=100)
        jobSummaries = response["TranscriptionJobSummaries"]
        jobs = []
        for jobSummary in jobSummaries:
            job = jobSummary["TranscriptionJobName"]
            jobs.append(job)
        return jobs

    def _delete_transcription_jobs(self, jobs):
        for job in jobs:
            print(job)
            self._client.delete_transcription_job(TranscriptionJobName=job)

    def delete_transcription_jobs(self):
        print("Deleting transcription jobs...")
        jobs = self._transcription_jobs()
        while jobs is not None and len(jobs) > 0:
            self._delete_transcription_jobs(jobs)
            jobs = self._transcription_jobs()

# Example use case of transcribing a recording using the client.        
def test_amazon_transcribe():
    bucket_client = AmazonBucketClient()
    recording_uri = bucket_client.mp3_recording_path("spanish2")
    print(recording_uri)
    
    transcribe_client = AmazonTranscribeClient()
    transcription = transcribe_client.transcribe_recording(recording_uri)
    print(transcription)

if __name__ == '__main__':
    client = AmazonTranscribeClient()
    client.delete_transcription_jobs()
    test_amazon_transcribe()