import boto3

ig_id = 'igw-0359124b54a0bc4dc'

ec2 = boto3.client('ec2')

ec2.delete_internet_gateway(
    InternetGatewayId=ig_id,
)
    