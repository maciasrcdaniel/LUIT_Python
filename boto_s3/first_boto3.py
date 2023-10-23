import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket='dmaciasboto3-10082023'
)

print(response)



