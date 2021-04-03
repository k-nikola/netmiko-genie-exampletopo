#! usr/bin/env python
from genie.testbed import load
from genie.utils.diff import Diff

#Creating a testbed object for the network from yml file
testbed = load("testbed.yml")

device = testbed.devices["CoreRouter"]
device.connect()

current_output = device.parse("show protocols")
diff = Diff(current_output, expected.output)
diff.findDiff()
print("Difference between the expected output and actual output:\n","-"*50,diff)

