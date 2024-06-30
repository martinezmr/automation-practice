import pandas as pd
from pprint import pprint as pp

data = [
    {
        "network_device": {
            "hostname": "spine1-nxos",
            "os_version": "9.3.7",
            "interface": [
                {"name": "eth0", "ip_address": "10.0.0.1"},
                {"name": "eth1", "ip_address": "10.0.0.2"},
            ],
        }
    },
    {
        "network_device": {
            "hostname": "spine2-nxos",
            "os_version": "9.3.7",
            "interface": [
                {"name": "eth0", "ip_address": "10.0.0.3"},
                {"name": "eth1", "ip_address": "10.0.0.4"},
            ],
        }
    },
]

df = pd.json_normalize(
    data=data,
    record_path=["network_device", "interface"],
    meta=[["network_device","hostname"], ["network_device","os_version"]]
    )

pp(df)