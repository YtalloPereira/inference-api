import json
from botocore.exceptions import ClientError

trust_policy = json.dumps(
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {"Service": "sagemaker.amazonaws.com"},
                "Action": "sts:AssumeRole",
            }
        ],
    }
)


def create_iam_role(iam_client, role_name):
    try:
        iam_client.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=trust_policy,
            Description="Total access for SageMaker and S3",
        )

        print(f"IAM role created")
    except ClientError as err:
        error_code = err.response["Error"]["Code"]

        if error_code == "EntityAlreadyExists":
            print(f"IAM Role already exists")
    except Exception as err:
        print(f"Error creating role: {err}")
