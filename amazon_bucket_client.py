#! /usr/bin/env python3.
# Client for interacting with the Amazon S3 Bucket API.
# Adapted from https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html.
from custom_filesystem import AMAZON_ACCESS_KEY_ID, AMAZON_SECRET_ACCESS_KEY, AMAZON_BUCKET_NAME
from botocore.exceptions import ClientError
import os
import boto3
import speech_accent_archive_analysis
from custom_filesystem import CustomFilesystem
from constants import MP3_EXTENSION

class AmazonBucketClient:
    def __init__(self):
        self._client = boto3.client(
            's3',
            aws_access_key_id = AMAZON_ACCESS_KEY_ID,
            aws_secret_access_key = AMAZON_SECRET_ACCESS_KEY,
            region_name = "us-east-1",
        )
    
    def create_bucket(self, bucket_name):
        self._client.create_bucket(Bucket=bucket_name)

    def list_buckets(self):
        response = self._client.list_buckets()
        buckets_response = response['Buckets']
        buckets = []
        for bucket_response in buckets_response:
            buckets.append(bucket_response['Name'])
        return buckets

    def upload_file(self, file_name, bucket_name, object_name=None):
        """Upload a file to an S3 bucket

        :param file_name: File to upload
        :param bucket: Bucket to upload to
        :param object_name: S3 object name. If not specified then file_name is used
        :return: True if file was uploaded, else False.
        """
        if object_name is None:
            object_name = os.path.basename(file_name)
        try:
            response = self.client.upload_file(file_name, bucket_name, object_name)
        except ClientError as e:
            return False
        return True
    
    def file_path(self, bucket_name, file_name):
        return os.path.join("s3://", bucket_name, file_name)
    
    def mp3_recording_path(self, file_without_extension):
        file_with_extension = file_without_extension + MP3_EXTENSION
        return self.file_path(AMAZON_BUCKET_NAME, file_with_extension)

# Adapted from https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html.
def speech_accent_archive_amazon_upload(client):
    recordings_per_language = speech_accent_archive_analysis.recordings_per_language()
    custom_filesystem = CustomFilesystem()
    for language, recordings in recordings_per_language.items():
        for recording in recordings:
            recording_path = custom_filesystem.mp3_recording_path(recording)
            client.aws_upload_file(recording_path, AMAZON_BUCKET_NAME)

# Example use case of the AmazonBucketClient.
def test_amazon_bucket():
    client = AmazonBucketClient()
    # client.create_bucket()
    buckets = client.list_buckets()
    print("Buckets in S3: ", end="")
    print(buckets)
    recording_path = client.mp3_recording_path("spanish2")
    print("Sample recording path " + recording_path)

if __name__ == '__main__':
    test_amazon_bucket()
    