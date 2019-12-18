from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import AuthenticationException
from paramiko.ssh_exception import SSHException
import sys
from getpass import getpass

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
'password': 'terOne1!',
}

host3 = {
'device_type': 'cisco_ios',
'ip': '10.4.3.1',
'username': 'Admin',
'password': 'NterOne1!',
}

routers = [host2, host3]
routers = [host1, host2, host3]

def tryconnect(target):
    try:
        print(target)
        return ConnectHandler(**target)
    except (AuthenticationException):
        print ('\n' + "*"*80)
        print ('Authentication Failure: ' + str(target))
        print ("*"*80)
        return 'AuthenticationException'
    except (NetMikoTimeoutException):
        print ('\n' + "*"*80)
        print ('Timeout to device: ' + str(target))
        print ("*"*80)
        return 'NetMikoTimeoutException'
    except (SSHException):
        print ('\n' + "*"*80)
        print ('SSH might not be enabled: ' + str(target))
        print ("*"*80)
        return 'SSHException'
    except (EOFError):
        print ('\n' + "*"*80)
        print ('End of attempting device: ' + str(target))
        print ("*"*80)
        return 'EOFError'
    except:
        print ('Some other error: ' + str(target) + str(sys.exc_info()))
        return 'Unknown error'

def execute_commands(net_connect, target):
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

for target in routers:
    net_connect = tryconnect(target)
    # print (net_connect)
    # print (type(net_connect))
    if net_connect == 'AuthenticationException':
        retry = input('Do you want to try entering the correct password? Y/N:  ').upper()
        if retry.startswith('Y'):
            newuser = input('Enter the same or new username:  ')
            newpw = getpass('Enter the correct password: ')
            target['username'] = newuser
            target['password'] = newpw
            net_connect = tryconnect(target)
    elif net_connect == 'NetMikoTimeoutException':
        retry = input('Do you want to retry entering the IP address? Y/N:  ').upper()
        if retry.startswith('Y'): 
            newip = input('Enter the correct IP address:  ')
            target['ip'] = newip
            net_connect = tryconnect(target)
    else:
        pass

    print (net_connect)
    if not isinstance(net_connect, str):
        execute_commands(net_connect, target)

