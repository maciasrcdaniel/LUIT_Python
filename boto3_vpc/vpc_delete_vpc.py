import boto3

ec2 = boto3.client('ec2')

vpc_id = 'vpc-074242d0754b30cba'

ec2.delete_vpc(
    VpcId=vpc_id,
)



