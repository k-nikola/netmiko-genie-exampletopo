#! usr/bin/env python
from genie.testbed import load
from genie.utils.diff import Diff
import json

#Creating a testbed object for the network from yml file
testbed = load("testbed.yml")

device = testbed.devices["CoreRouter"]
device.connect()
with open("expected_status.json") as es:
    expected_status = json.loads(es.read())
current_interface_status = device.parse("show ip int brief")
diff = Diff(current_interface_status, expected_status)
diff.findDiff()
print("Difference between the expected output and actual output:\n","-"*50,diff)