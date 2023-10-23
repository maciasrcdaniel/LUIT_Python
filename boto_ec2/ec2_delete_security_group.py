import boto3

sg_group_id = 'sg-02dfc12af2ed31096'

ec2 = boto3.client('ec2')

response = ec2.delete_security_group(
    GroupId=sg_group_id,
)

print(sg_group_id, 'deleted')