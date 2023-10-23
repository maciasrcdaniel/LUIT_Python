import boto3

s3 = boto3.client('s3')

response = s3.list_objects(Bucket='dmaciasboto3-10082023')

content = response['Contents']

for item in content: 
    print(item['Key'], ' - ', item['LastModified'])
    
