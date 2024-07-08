from botocore.exceptions import ClientError

def create_rds_instance(
    rds_client,
    db_instance_identifier,
    db_name,
    master_password,
    master_username,
):
    try:
        rds_client.create_db_instance(
            DBName=db_name,
            DBInstanceIdentifier=db_instance_identifier,
            AllocatedStorage=20,
            DBInstanceClass="db.t3.micro",
            Engine="mysql",
            MasterUsername=master_username,
            MasterUserPassword=master_password,
        )

        print(f"RDS Instance {db_instance_identifier} created")
    except ClientError as err:
        error_code = err.response["Error"]["Code"]

        if error_code == "DBInstanceAlreadyExists":
            print(f"RDS Instance {db_instance_identifier} already exists")
    except Exception as err:
        print(f"Error creating RDS Instance: {err}")
