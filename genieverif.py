#! usr/bin/env python
from genie.testbed import load
from genie.utils.diff import Diff
import json

#Creating a testbed object for the network from yml file
testbed = load("testbed.yml")


device = testbed.devices["CoreRouter"]
device.connect()

current_interface_status = device.parse("show protocols")
diff = Diff(current_interface_status, expected_interface_status)
diff.findDiff()
print("Difference between the expected output and actual output:\n","-"*50,diff)

