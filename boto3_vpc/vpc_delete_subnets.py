import boto3

ec2 = boto3.client('ec2')


subnet_id = 'subnet-0a53a9466863b60e7'

response = ec2.delete_subnet(
    SubnetId=subnet_id,
)

