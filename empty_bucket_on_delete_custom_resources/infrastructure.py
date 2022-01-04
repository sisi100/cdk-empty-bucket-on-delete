import pathlib

from aws_cdk import CustomResource, Duration
from aws_cdk.aws_lambda import Code, Function, Runtime
from aws_cdk.aws_s3 import Bucket
from aws_cdk.custom_resources import Provider
from constructs import Construct


class EmptyBucketOnDeleteCustomResources(Construct):
    def __init__(self, scope: Construct, construct_id: str, *, bucket: Bucket) -> None:
        super().__init__(scope, construct_id)

        on_event = Function(
            self,
            "CustomResourcesLambda",
            code=Code.from_asset(str(pathlib.Path(__file__).resolve().parent.joinpath("runtime"))),
            runtime=Runtime.PYTHON_3_9,
            timeout=Duration.seconds(60),
            handler="index.on_event",
            environment={"BUCKET_NAME": bucket.bucket_name},
        )
        bucket.grant_read(on_event)  # `ListObjects`するために必要
        bucket.grant_delete(on_event)

        provider = Provider(self, "Provider", on_event_handler=on_event)
        CustomResource(
            self,
            "CustomResource",
            service_token=provider.service_token,
        )
