import boto3 


def filter_object_extension(client, bucket, extension):
    keys = []
    response = client.list_objects_v2(Bucket=bucket)
    for content in response['Contents']:
        if(extension in content['Key'][-(len(extension)):]): 
            keys.append(content['Key'])
    return keys
    
    
    
def list_object_keys(client, bucket, prefix=""):
    keys = []
    response = client.list_objects_v2(Bucket=bucket, Prefix=prefix)
    for content in response['Contents']: 
        keys.append(content['Key'])
    return keys
    
    
    
if __name__ == '__main__': 
    s3 = boto3.client('s3')
    
    response = filter_object_extension(s3, 'dmaciasboto3-10082023', ".txt")
    print(response)
    
    
    response_v2 = list_object_keys(s3, 'dmaciasboto3-10082023')
    print(response_v2)