import boto3

s3 = boto3.client('s3')

with open("test_text.txt", 'rb') as f: 
    s3.put_object(Bucket="dmaciasboto3-10082023", Key="test_text.txt", Body=f, ContentType="text/plain")

