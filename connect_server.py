from subprocess import *
import os
import time
import sys
import paramiko
host='hostname' #hostname or IP address (ifconfig or (hostname and dnsdomainname))
user = 'username'#username (whoami)
passd = 'password' #password for login into server
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host, username=user, password=passd)
shell = ssh.invoke_shell()
##shell.send(command + "\n")
stdin, stdout, stderr = ssh.exec_command('pwd')
output = []
for i in range(0,6):
  output.append(stdout.readlines(i))
print(output)
