
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('ec2-3-39-117-244.ap-northeast-2.compute.amazonaws.com', port='22', username='ubuntu', key_filename='/Users/chance/pem/act-cicd-seoul.pem')

stdin, stdout, stderr = ssh.exec_command('ls')
stdin, stdout, stderr = ssh.exec_command('ls')

print("stdin : {}".format(stdin))
print("stdout : {}".format(stdout))
print("stderr : {}".format(stderr))
print(''.join(stdout.readlines()))

ssh.close()