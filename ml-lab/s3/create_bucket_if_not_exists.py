def create_s3_bucket_if_not_exists(s3_client, bucket):
    try:
        s3_client.get_bucket_acl(Bucket=bucket)
        print(f"S3 Bucket founded")
    except s3_client.exceptions.NoSuchBucket:
        print("S3 Bucket not found")
        s3_client.create_bucket(Bucket=bucket)
        print(f"S3 Bucket created")
