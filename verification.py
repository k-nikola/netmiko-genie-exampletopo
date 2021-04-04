#!/usr/bin/env python

#Importing important modules, packages, libraries
import datetime
from netmiko import ConnectHandler

#region Defining all of the network devices in the topology
CoreRouter = {
   'device_type': 'cisco_ios',
   'ip': '192.168.121.1',
   'username': 'nikola',
   'password': 'cisco',
}
#endregion

#Grouping verification commands in a list
vf_cmd = ['show protocols','show ip route']
#Connecting to the router
net_connect = ConnectHandler(**CoreRouter)
#Sending the configuration verification commands and printing the results
i = 1
for cmd in vf_cmd:
   output = net_connect.send_command(cmd) + "\n"
   with open('ios_router_expected'+str(i)) as router_expected:
      expected = router_expected.read().splitlines()
      expected_output = ""
      for line in expected:
         expected_output+= str(line) + "\n"
   if output!= expected_output:
      print("Configuration seems to be different than expected.")
      print("Expected output: \n",expected_output)
      print("Actual output: \n",output)
   else:
      print("Configuration seems to be as expected.")
   i+=1
net_connect.disconnect()
