from botocore.exceptions import ClientError


def get_rds_instance(rds_client, db_instance_identifier):
    try:
        response = rds_client.describe_db_instances(
            DBInstanceIdentifier=db_instance_identifier
        )
        db_instances = response["DBInstances"]
        db_instance = db_instances[0]

        print(f"RDS Instance founded")

        endpoint = db_instance["Endpoint"]["Address"]
        return endpoint
    except ClientError as err:
        error_code = err.response["Error"]["Code"]

        if error_code == "DBInstanceNotFound":
            print(f"RDS Instance not found")
    except Exception as err:
        print(f"Error accessing RDS Instance: {err}")
