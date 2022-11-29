#python_paramiko.py

import paramiko
import yaml, json
ssh = 0

def connect():
    global ssh
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('ec2-3-39-117-244.ap-northeast-2.compute.amazonaws.com', port='22', username='ubuntu', key_filename='/Users/chance/pem/act-cicd-seoul.pem')
    return True

def disconnect():
    global ssh
    ssh.close()
    return True


def dfh():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('ec2-3-39-117-244.ap-northeast-2.compute.amazonaws.com', port='22', username='ubuntu', key_filename='/Users/chance/pem/act-cicd-seoul.pem')

    stdin, stdout, stderr = ssh.exec_command('df -h')
    result = ''.join(stdout.readlines())
    ssh.close()
    print(result)
    return result


def getAllPod():
    # ssh = paramiko.SSHClient()
    # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ssh.connect('ec2-3-39-117-244.ap-northeast-2.compute.amazonaws.com', port='22', username='ubuntu', key_filename='/Users/chance/pem/act-cicd-seoul.pem')

    stdin, stdout, stderr = ssh.exec_command('kubectl get all -n beast')
    result = ''.join(stdout.readlines())
    # ssh.close()
    print(result)
    return result

def getAllNamespace():
    # ssh = paramiko.SSHClient()
    # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ssh.connect('ec2-3-39-117-244.ap-northeast-2.compute.amazonaws.com', port='22', username='ubuntu', key_filename='/Users/chance/pem/act-cicd-seoul.pem')

    stdin, stdout, stderr = ssh.exec_command('kubectl get ns')
    result = ''.join(stdout.readlines())
    a = result.splitlines()
    a.pop(0)
    nsList = list()
    for i in a:
        splitLine = " ".join(i.split()).split(" ")
        data = {"ns" :  splitLine[0], "status" : splitLine[1], "age" : splitLine[2]}
        nsList.append(data)
    
    print(nsList)
    # ssh.close()
    return nsList


def getClusterInfo():
    stdin, stdout, stderr = ssh.exec_command('kubectl config view')
    result = ''.join(stdout.readlines())
    dct = yaml.safe_load(result)
    name = dct["users"][0]["name"]
    
    sp = name.split(':')
    # region = sp[3]
    # aws_user = sp[4]
    # spp = sp[5].split('/')
    # cluster_name = spp[1]
    ret = {}
    ret['region'] = sp[3]
    ret['aws_user'] = sp[4]
    ret['cluster_name'] = sp[5].split('/')[1]
    
    resList = []
    resList.append(ret)
    return resList