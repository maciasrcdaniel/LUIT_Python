import boto3


ig_id = 'igw-0359124b54a0bc4dc'
vpc_id = 'vpc-074242d0754b30cba'

ec2 = boto3.client('ec2')

ec2.attach_internet_gateway(
    InternetGatewayId=ig_id,
    VpcId=vpc_id
)
