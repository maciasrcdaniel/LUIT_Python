import boto3
import os 
from boto3_list_objects_v2 import list_object_keys


# download file function
def download_single_object(client, bucket, key, filename):
    client.download_file(bucket, key, filename)

if __name__ == '__main__':

    bucket = 'dmaciasboto3-10082023'
    key = 'test_text.txt'
    client = 's3'
    filename = 'test_text.txt'
    
    
    s3 = boto3.client('s3')
    
        
    keys = list_object_keys(s3, bucket, prefix='folder') 
    
    for key in keys:
        if '/' == key[-1]:
            try:
                os.mkdir(key)
            except: 
                pass
        else:
            download_single_object(s3, bucket, key, key)
            
        