import time
from paramiko import HostKeys
import requests

class DNACRequestor:

    def __init__(self, host, username, password, verify=True, old_style=False):

        self.host = host
        self.verify = verify

        if not verify:
            requests.packages.urllib3.disable_warnings()

        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        if old_style:
            auth_url = "api/system/v1/auth/token"
        else:
            auth_url = "dna/system/api/v1/auth/token"

        auth_resp = self.req(auth_url, method="post", auth=(username, password))
        auth_resp.raise_for_status()
        self.headers["X-Auth-Token"] = auth_resp.json()["Token"]

def req(
    self,
    resource,
    method
)