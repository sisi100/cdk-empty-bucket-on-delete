from aws_cdk import Stack  # Duration,; aws_sqs as sqs,
from constructs import Construct

from empty_bucket_on_delete_custom_resources.infrastructure import EmptyBucketOnDeleteCustomResources
from sample_bucket.infrastructure import SampleBucket


class CdkEmptyBucketOnDeleteStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Sampleバケットを作る
        sample_bucket_stack = Stack(self, "SampleBucketStack")
        sample_bucket = SampleBucket(sample_bucket_stack, "SampleBucket")

        # stack削除時にバケットを空にするカスタムポリシーを作る
        empty_bucket_on_delete_custom_resources_stack = Stack(self, "EmptyBucketOnDeleteCustomResourcesStack")
        EmptyBucketOnDeleteCustomResources(
            empty_bucket_on_delete_custom_resources_stack,
            "EmptyBucketOnDeleteCustomResources",
            bucket=sample_bucket.bucket,
        )

        # Stackの依存関係を定義する
        empty_bucket_on_delete_custom_resources_stack.add_dependency(sample_bucket_stack)
