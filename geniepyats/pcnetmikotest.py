import concurrent.futures
import os
import time

from dotenv import load_dotenv
from netmiko import ConnectHandler
from rich import print

load_dotenv()

STARTTIME = time.time()

DEVICE_OUTPUT = dict()

THREADS = 20

USERNAME = os.getenv("LAB_USERNAME")
PASSWORD = os.getenv("LAB_PASSWORD")
DEVICES = [
    {"host": "172.29.151.1", "device_type": "cisco_nxos"},
    {"host": "172.29.151.2", "device_type": "cisco_nxos"},
    {"host": "172.29.151.3", "device_type": "cisco_ios"},
    {"host": "172.29.151.4", "device_type": "cisco_ios"},
    {"host": "172.29.151.5", "device_type": "juniper_junos"},
    {"host": "172.29.151.6", "device_type": "juniper_junos"},
    {"host": "172.29.151.7", "device_type": "arista_eos"},
    {"host": "172.29.151.8", "device_type": "arista_eos"},
]


def collect_data(device):
    print(f"Connecting | {device['host']} - {device['device_type']}")

    device = {
        "host": device["host"],
        "username": USERNAME,
        "password": PASSWORD,
        "device_type": device["device_type"],
        "fast_cli": False,
    }

    connection = ConnectHandler(**device)
    connection.enable()

    output = connection.send_command("show version")

    DEVICE_OUTPUT.update({f"{device['host']}": output})

    connection.disconnect()

    print(f"Complete | {device['host']} - {device['device_type']}")


if __name__ == "__main__":
    for port_device_type in DEVICES:
        collect_data(port_device_type)

    print("===========")
    print(DEVICE_OUTPUT)
    print("===========")
    print("Total time:", time.time() - STARTTIME)