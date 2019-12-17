from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import AuthenticationException
from paramiko.ssh_exception import SSHException
import sys

host1 = {
'device_type': 'cisco_ios',
'ip': '10.4.0.17',
'username': 'Admin',
'password': 'NterOne1!',
}

host2 = {
'device_type': 'cisco_ios',
'ip': '10.4.1.1',
'username': 'Admin',
'password': 'NterOne1!',
}

host3 = {
'device_type': 'cisco_ios',
'ip': '10.4.3.1',
'username': 'Admin',
'password': 'NterOne1!',
}

#routers =[host1, host2, host3]
routers =[host3]

for target in routers:
    try:
        net_connect = ConnectHandler(**target)
        print(target)
    except (AuthenticationException):
        print ('\n' + "*"*80)
        print ('Authentication Failure: ' + str(target))
        print ("*"*80)
        continue
    except (NetMikoTimeoutException):
        print ('\n' + "*"*80)
        print ('Timeout to device: ' + str(target))
        print ("*"*80)
        continue
    except (SSHException):
        print ('\n' + "*"*80)
        print ('SSH might not be enabled: ' + str(target))
        print ("*"*80)
        continue
    except (EOFError):
        print ('\n' + "*"*80)
        print ('End of attempting device: ' + str(target))
        print ("*"*80)
        continue
    except:
        print ('Some other error: ' + str(target) + str(sys.exc_info()))

    loopback11 = "11.4."+target['ip'].split('.')[2]+'.1'
    loopbackcmd = 'ip address '+ loopback11+ ' 255.255.255.0'
    config_commands = ['int loop 11', loopbackcmd]
    output = net_connect.send_config_set(config_commands)
    print (output)
    print ("-"*20)
    
    output = net_connect.send_command('show ip int brief')
    print (output)
    print ("="*80)
    
    net_connect.disconnect()

