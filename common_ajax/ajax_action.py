#!/usr/bin/env python
# coding=utf-8
"""
    Copyright (c) 2016 wjika, Inc. All Rights Reserved
    @author: xuchu(xuchu@acfun.tv)
"""
import paramiko
def ssh_qa_server(command):
    '''ssh登陆测试服务器并执行shell命令'''
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='192.168.71.101', port=22, username='root', password='MdxBlsntKb7')
    stdin, stdout, stderr = ssh.exec_command(command)
    results = stdout.readlines()
    print results
    ssh.close()
    return results

# Go
if __name__ == '__main__':
    ssh_qa_server(command='pwd')