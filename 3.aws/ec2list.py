import boto3
ec2 = boto3.resource('ec2')
for instance in ec2.instances.all():
    print(
         "Id: {0}\nType: {1}\nPublic IPv4: {2}\nAMI: {3}\nState: {4}\n".format(
         instance.id, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state
         )
    )