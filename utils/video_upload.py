import boto3
from botocore.exceptions import NoCredentialsError
from dotenv import load_dotenv
import os

load_dotenv()

ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
SECRET_KEY = os.getenv('AWS_SECRET_KEY')
BUCKET_NAME = "cfg-team1"


def upload_file(file_data, file_name):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(file_data, BUCKET_NAME, file_name)
        return True, file_name
    except FileNotFoundError:
        print("The file was not found")
        return False, None
    except NoCredentialsError:
        print("Credentials not available")
        return False, None