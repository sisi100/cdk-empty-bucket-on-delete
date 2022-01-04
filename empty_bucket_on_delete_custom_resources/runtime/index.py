import os

import boto3


def on_event(event, context):
    if event["RequestType"] == "Delete":
        if bucket_name := os.getenv("BUCKET_NAME"):
            s3 = boto3.resource("s3")
            bucket = s3.Bucket(bucket_name)
            bucket.objects.all().delete()
