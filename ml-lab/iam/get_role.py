from botocore.exceptions import ClientError

def get_iam_role(iam_client, role_name):
    try:
        response = iam_client.get_role(RoleName=role_name)
        
        print(f"IAM Role founded")

        role = response["Role"]["Arn"]
        return role
    except ClientError as err:
        error_code = err.response["Error"]["Code"]

        if error_code == "NoSuchEntity":
            print(f"IAM Role not found")
    except Exception as err:
        print(f"Error getting Role: {err}")
