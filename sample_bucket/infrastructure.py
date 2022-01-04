import pathlib

from aws_cdk import RemovalPolicy
from aws_cdk.aws_s3 import Bucket
from aws_cdk.aws_s3_deployment import BucketDeployment, Source
from constructs import Construct


class SampleBucket(Construct):
    @property
    def bucket(self):
        return self._bucket

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id)

        bucket = Bucket(
            self,
            "Bucket",
            removal_policy=RemovalPolicy.DESTROY,
        )

        BucketDeployment(
            self,
            "BucketDeployment",
            sources=[Source.asset(str(pathlib.Path(__file__).resolve().parent.joinpath("sample_data")))],
            destination_bucket=bucket,
        )
        self._bucket = bucket
