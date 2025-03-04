import boto3
import os

s3 = boto3.client(
    's3',
    endpoint_url='https://in-maa-1.linodeobjects.com',
     aws_access_key_id='PEY1N8YWN4PXQ72SHDE8',
    aws_secret_access_key='x1hyxqtUYR2fTCcyiUUIxJoQ7ttVEDlxdqKpDxPm'
)

bucket_name = "alumni"
folder_prefix = "alumnis/"  # Folder in S3
download_path = os.path.expanduser("~/Downloads")  # Change to a writable directory

# Ensure the directory exists
if not os.path.exists(download_path):
    os.makedirs(download_path)

# List all objects in the folder
response = s3.list_objects_v2(Bucket=bucket_name, Prefix=folder_prefix)

if 'Contents' in response:
    for obj in response['Contents']:
        file_key = obj['Key']
        file_name = os.path.join(download_path, os.path.basename(file_key))
        
        print(f"Downloading {file_key} to {file_name}...")
        try:
            s3.download_file(bucket_name, file_key, file_name)
            print(f"Downloaded: {file_name}")
        except Exception as e:
            print(f"Error downloading {file_key}: {e}")
else:
    print("No files found in the 'alumnis/' folder!")
