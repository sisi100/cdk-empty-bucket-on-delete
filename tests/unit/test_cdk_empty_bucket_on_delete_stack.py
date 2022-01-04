import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_empty_bucket_on_delete.cdk_empty_bucket_on_delete_stack import CdkEmptyBucketOnDeleteStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_empty_bucket_on_delete/cdk_empty_bucket_on_delete_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkEmptyBucketOnDeleteStack(app, "cdk-empty-bucket-on-delete")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
