from netmiko import ConnectHandler

host1 = {
'device_type': 'cisco_ios',
'ip': '10.4.0.1',
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

routers =[host1, host2, host3]

#for target in routers:
#    net_connect = ConnectHandler(**target)
#    print(target)
#    output = net_connect.send_command('show ip int brief')
#    print(output)
#    
#    loopback11 = "11.4."+target['ip'].split('.')[2]+'.1'
#    loopbackcmd = 'ip address '+ loopback11+ ' 255.255.255.0'
#    config_commands = ['int loop 11', loopbackcmd]
#    output = net_connect.send_config_set(config_commands)
#    print(output)
#    
#    output = net_connect.send_command('show ip int brief')
#    print(output)
#    
#    net_connect.disconnect()

for target in routers:
    net_connect = ConnectHandler(**target)

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