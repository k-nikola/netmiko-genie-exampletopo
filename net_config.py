#!/usr/bin/env python

#Importing important modules, packages, libraries
from netmiko import ConnectHandler

#region Defining all of the network devices in the topology
CoreSW1 = {
   'device_type': 'cisco_ios',
   'ip': '192.168.121.3',
   'username': 'nikola',
   'password': 'cisco',
}
CoreSW2 = {
   'device_type': 'cisco_ios',
   'ip': '192.168.121.4',
   'username': 'nikola',
   'password': 'cisco',
}
AccessSW1 = {
   'device_type': 'cisco_ios',
   'ip': '192.168.121.5',
   'username': 'nikola',
   'password': 'cisco',
}
AccessSW2 = {
   'device_type': 'cisco_ios',
   'ip': '192.168.121.6',
   'username': 'nikola',
   'password': 'cisco',
}
CoreRouter = {
   'device_type': 'cisco_ios',
   'ip': '192.168.121.1',
   'username': 'nikola',
   'password': 'cisco',
}
#endregion
#Grouping access devices into a list
access_devices = [AccessSW1, AccessSW2]
#Counter used to recall adequate device configuration file
i = 1

#Looping through all the access devices in the topology
for device in access_devices:
   #Getting the access device configuration files ready
   with open('ios_access'+str(i)+'_config') as cfg:
      access_cfg = cfg.read().splitlines()
      print(access_cfg)
   #Connecting to the access device
   net_connect = ConnectHandler(**device)
   output = net_connect.send_config_set(access_cfg)
   print(output)
   i = i + 1

#Getting the core device configuration file ready
with open('ios_core_config') as cfg:
   core_cfg = cfg.read().splitlines()
   print(core_cfg)
#Grouping core devices into a list
#core_devices = [CoreSW2, CoreSW1]
core_devices = [CoreSW1]
#Looping through all the core devices in the topology
for device in core_devices:
   #Connecting to the core device
   net_connect = ConnectHandler(**device)
   output = net_connect.send_config_set(core_cfg)
   print(output)

#Getting the router configuration file ready
with open('ios_router_config') as cfg:
   router_cfg = cfg.read().splitlines()
   print(router_cfg)
#Connecting to the router
net_connect = ConnectHandler(**CoreRouter)
#Sending the configuration commands and printing the results
output = net_connect.send_config_set(router_cfg, delay_factor=5)
print(output)
net_connect.disconnect()
