#!/usr/bin/env python

import os
import requests
import yaml

with open("config.yml", "r") as config_file:
    config = yaml.safe_load(config_file)

IP_RECORD = "/tmp/ddns-ip-record"
recorded_ip = None
if os.path.exists(IP_RECORD):
    with open(IP_RECORD, "r") as f:
        recorded_ip = f.read().strip()

try:
    public_ip = requests.get("https://api.ipify.org").text.strip()
except requests.RequestException as e:
    print("Error fetching IP:", e)
    exit(1)

if public_ip == recorded_ip:
    print("IP has not changed")
    exit(0)

with open(IP_RECORD, "w") as f:
    f.write(public_ip)

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {config['BEARER_TOKEN']}",
}
record = {
    "type": "A",
    "name": config["A_RECORD_NAME"],
    "content": public_ip,
    "ttl": config["A_RECORD_TTL"],
    "proxied": config["A_RECORD_PROXIED"],
}
url = f"https://api.cloudflare.com/client/v4/zones/{config['ZONE_ID']}/dns_records/{config['A_RECORD_ID']}"  # noqa E501
try:
    response = requests.patch(url, json=record, headers=headers)
    response.raise_for_status()
except requests.RequestException as e:
    print("Error updating DNS record:", e)
    exit(1)
