#python_paramiko.py

import paramiko


def dfh():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('ec2-3-39-117-244.ap-northeast-2.compute.amazonaws.com', port='22', username='ubuntu', key_filename='/Users/chance/pem/act-cicd-seoul.pem')

    stdin, stdout, stderr = ssh.exec_command('df -h')
    result = ''.join(stdout.readlines())
    ssh.close()
    print(result)
    return result
