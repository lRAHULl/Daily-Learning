
import aws_constants

import boto3
import json
import requests

s3 = boto3.client('s3',
                  aws_access_key_id = aws_constants.AWS_ACCESS_KEY,
                  aws_secret_access_key = aws_constants.AWS_SECRET_KEY,
                  region_name='eu-north-1')

BUCKET_NAME = 's3-test-bucket-for-learning'
OBJECT_NAME = 'cat.png'
EXPIRES_IN  = 10

presigned_post_response = s3.generate_presigned_post(Bucket = BUCKET_NAME,
                                                     Key = OBJECT_NAME,
                                                     ExpiresIn=EXPIRES_IN)

print(json.dumps(presigned_post_response))

files = { 'file': open(OBJECT_NAME, 'rb') }

print(files)

post_to_s3_response = requests.post(url=presigned_post_response['url'],
                                    data=presigned_post_response['fields'],
                                    files=files)

print(post_to_s3_response.status_code, post_to_s3_response.content)
