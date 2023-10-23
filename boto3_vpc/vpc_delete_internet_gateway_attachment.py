import boto3

internet_gateway = 'igw-0359124b54a0bc4dc'
vpc_id = 'vpc-074242d0754b30cba'

ec2 = boto3.client('ec2')

ec2.detach_internet_gateway(
    VpcId=vpc_id,
    InternetGatewayId=internet_gateway,
)

