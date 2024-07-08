import os
from dotenv import load_dotenv

load_dotenv(override=True)

required_env_vars = [
    "RDS_USER",
    "RDS_PASSWORD",
    "RDS_DB_NAME",
    "RDS_INSTANCE_NAME",
    "AWS_PROFILE_NAME",
]
missing_vars = [var for var in required_env_vars if not os.getenv(var)]

if missing_vars:
    raise EnvironmentError(
        f"Environment variables {', '.join(missing_vars)} are necessary."
    )

AWS_PROFILE_NAME: str = os.getenv("AWS_PROFILE_NAME")
RDS_USER: str = os.getenv("RDS_USER")
RDS_PASSWORD: str = os.getenv("RDS_PASSWORD")
RDS_DB_NAME = os.getenv("RDS_DB_NAME")
RDS_INSTANCE_NAME: str = os.getenv("RDS_INSTANCE_NAME")
