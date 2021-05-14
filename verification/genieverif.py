#! usr/bin/env python
from genie.testbed import load
from genie.utils.diff import Diff
import json

#Creating a testbed object for the network from yml file
testbed = load("testbed.yml")

#Creating a variable that points to a device in the yml file
device = testbed.devices["CoreRouter"]
#Opening an SSH connection to the device(SSH parameters are set inside the yml file).
device.connect()

#Loading expected interface statuses from a json file. Saving it inside a dict variable.
with open("expected_status.json") as es:
    expected_status = json.loads(es.read())
    
#Saving the informations about interface status inside a variable
current_interface_status = device.parse("show ip int brief")
#Passing the two status information variables inside a new variable
diff = Diff(current_interface_status, expected_status)
#Finding the difference between the two, and printing it.
diff.findDiff()
print("Difference between the expected output and actual output:\n","-"*50,diff)

