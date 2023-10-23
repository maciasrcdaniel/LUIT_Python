import boto3




ec2 = boto3.client('ec2')

response = ec2.create_image(
    InstanceId='i-0e224fdf258621bfe',
    Name='Go to AMI'
)

print(response['ImageId'])


