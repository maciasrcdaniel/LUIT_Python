import boto3

ami_id = 'ami-00bf972d4e6bc0213'

ec2 = boto3.client('ec2')


response = ec2.deregister_image(
    ImageId=ami_id,
)

print(ami_id, 'deregistered')