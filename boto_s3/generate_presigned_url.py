import boto3

s3 = boto3.client('s3')

response = s3.generate_presigned_url('get_object', Params={'Bucket':'dmaciasboto3-10082023', 'Key':'test_text.txt'}, ExpiresIn=3600)

print(response)