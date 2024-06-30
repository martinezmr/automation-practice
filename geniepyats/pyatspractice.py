from dotenv import load_dotenv
from genie import testbed

# Load .env into environment variables
load_dotenv()

# Load the testbed
testbed = testbed.load("./testbeds/testbed.yml")

# Select the device we want to test
device = testbed.devices["leaf1-ios"]

# Connect to device
device.connect()

# Parse - show ip interface brief
ip_interface_brief_output = device.parse("show ip interface brief")
Shell