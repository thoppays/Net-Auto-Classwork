import paramiko
import time

routers = routers = ["10.4.0.1", "10.4.1.2", "10.4.3.3"]
username = "Admin"
password = "NterOne1!"

sshcon = paramiko.SSHClient()
sshcon.set_missing_host_key_policy(paramiko.AutoAddPolicy())
for target in routers:
    sshcon.connect(hostname=target,username=username,password=password)
    print ("Successful connection", target)
    remote_connection = sshcon.invoke_shell()
    loopback10 = "10.4."+target.split('.')[2]+'.100'
    loopbackcmd = 'ip address '+ loopback10+ ' 255.255.255.0'
    remote_connection.send("configure terminal\n")
    remote_connection.send("int loop 10\n")
    remote_connection.send(loopbackcmd+"\n")
    remote_connection.send("end\n")
    time.sleep(1)
    output = remote_connection.recv(65535)
    print (output.decode('utf-8'))
    sshcon.close
print("Job completed succesfully")