import tarfile
from dotenv import load_dotenv
import boto3
import os

load_dotenv(override=True)

# Environment variables
profile_name = os.getenv("AWS_PROFILE_NAME")
bucket = os.getenv("S3_BUCKET_NAME")

# Boto3 session
boto_session = boto3.Session(profile_name=profile_name)

# Clients
sagemaker_client = boto_session.client("sagemaker")
s3_client = boto_session.client("s3")

# S3 subfolders
subfolder_model: str = "models/hotel-reservations/xgboost"

# Get the last training job
response = sagemaker_client.list_training_jobs(
    SortBy="CreationTime", SortOrder="Descending", MaxResults=1
)

# Get the last training job name
last_training_job_name: str = response["TrainingJobSummaries"][0]["TrainingJobName"]

# S3 paths
s3_model_data: str = f"{subfolder_model}/{last_training_job_name}/output/model.tar.gz"

# Local paths
zipped_model_folder: str = "model.tar.gz"
xgboost_model_file: str = "xgboost-model"

# Download the model and test data
s3_client.download_file(bucket, s3_model_data, zipped_model_folder)

# Extract the model
with tarfile.open(zipped_model_folder) as tar:
    tar_list = tar.getnames()
    print("Files in the tar archive:", tar_list)

    # Extract all files
    tar.extractall()

if os.path.exists(xgboost_model_file):
    with open(xgboost_model_file, "rb") as f:
        file_header = f.read(4)
        print("File header:", file_header)

os.remove(zipped_model_folder)
