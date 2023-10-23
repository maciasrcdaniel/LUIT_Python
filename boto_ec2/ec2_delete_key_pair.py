import boto3

key_pair_name = 'Key from boto3'

ec2 = boto3.client('ec2')

response = ec2.delete_key_pair(
    KeyName=key_pair_name,
)

print(key_pair_name, 'deleted')