"""
Thin wrapper around boto3 pointed at MinIO instead of real AWS S3.

Because MinIO speaks the S3 API, this exact same client code works
unmodified against real S3 -- you'd only change the endpoint_url and
credentials (or drop endpoint_url entirely to hit AWS).
"""
import os

import boto3
from botocore.client import Config

BUCKET_NAME = os.environ.get("MINIO_BUCKET", "raw-weather")


def get_minio_client():
    endpoint = os.environ.get("MINIO_ENDPOINT", "http://localhost:9000")
    access_key = os.environ.get("MINIO_ACCESS_KEY", "minioadmin")
    secret_key = os.environ.get("MINIO_SECRET_KEY", "minioadmin")
    return boto3.client(
        "s3",
        endpoint_url=endpoint,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        config=Config(signature_version="s3v4"),
        region_name="us-east-1",
    )
