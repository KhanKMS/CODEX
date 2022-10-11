## 인바운드가 Any로 설정된 Security 그룹 확인 

import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

def sg_check():
    response = ec2.describe_security_groups()['SecurityGroups']

    for i in response:
        sgid = i['GroupId']
        for j in i['IpPermissions']:
            try:
                port = 'ANY' if j['FromPort'] == -1 else j['FromPort']
                protocol = j['IpProtocol']
                ipaddr = j['IpRanges'][0]['CidrIp']

                if ipaddr == '0.0.0.0/0':   # ip가 any 인것을 나열함. 
                    print('sgid : %s, port : %s, protocol : %s, ipaddr : %s' %(sgid,port,protocol,ipaddr))

            except:
                pass

if __name__ == "__main__":
    sg_check()