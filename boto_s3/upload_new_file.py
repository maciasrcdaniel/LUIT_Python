import boto3

s3 = boto3.client('s3')

s3.put_object(Bucket='dmaciasboto3-10082023', 
                Key='folder/foldera/folder1/test_text_string.txt', 
                Body="This is a test upload fora new object", 
                ContentType='text/plain')
