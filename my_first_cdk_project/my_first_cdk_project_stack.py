from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_s3 as _s3,
    aws_iam as _iam
)

import aws_cdk as core
from constructs import Construct

class MyFirstCdkProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        _s3.Bucket(
            self,
            "myBucketId",
            bucket_name="cdkproject",
            versioned=True,
            encryption=_s3.BucketEncryption.KMS_MANAGED


        )

        mybucket = _s3.Bucket(
            self,
            "myBucketId1"
 
        )

        snstopicname= "abcdfs34"

        if not core.Token.is_unresolved(snstopicname) and len(snstopicname) > 10:
            raise ValueError("maximum value can be only 10 characters")
        
        print(mybucket.bucket_name)

        _iam.Group(
            self,
            "gid"
        )
 
        output_1 = core.CfnOutput(
            self,
            "myBucketOutput1",
            value=mybucket.bucket_name,
            description=f"My first s3 bucket",
            export_name= "myBucketOutput1"
        )

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "MyFirstCdkProjectQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
