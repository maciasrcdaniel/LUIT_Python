import boto3

def empty_bucket(client, bucket): 
    response = client.list_objects_v2(Bucket=bucket)
    
    if 'Contents' in response:
        objects = [{'Key': content['Key']} for content in response['Contents']]

        response = client.delete_objects(
            Bucket=bucket,
            Delete={
                'Objects':objects
            }
        )
        
        while response.get('NextContinuationToken'): 
            response = client.list_object_v2(Bucket=bucket, 
                        ContinuationToken=response['NextContinuationToken'])

            objects = [{'Key': content['Key']} for content in response['Contents']]

            response = client.delete_objects(
                Bucket=bucket,
                Delete={
                    'Objects':objects
                }
            )
            
def delete_empty_bucket(client, bucket): 
    response = client.delete_bucket(
        Bucket=bucket
)

s3 = boto3.client('s3')

bucket = 'dmaciasboto3-10082023'

empty_bucket(s3, bucket)
delete_empty_bucket(s3, bucket)