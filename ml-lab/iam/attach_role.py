from botocore.exceptions import ClientError


def attach_iam_role(iam_client, role_name):
    try:
        iam_client.attach_role_policy(
            RoleName=role_name,
            PolicyArn="arn:aws:iam::aws:policy/AmazonSageMakerFullAccess",
        )

        iam_client.attach_role_policy(
            RoleName=role_name, 
            PolicyArn="arn:aws:iam::aws:policy/AmazonS3FullAccess"
        )

        print(f"IAM Role attached with sagemaker and s3 full access")
    except ClientError as err:
        error_code = err.response["Error"]["Code"]

        if error_code == "NoSuchEntity":
            print(f"IAM Role not found")
    except Exception as err:
        print(f"Error attaching Role: {err}")
