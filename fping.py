import sys, time, requests, json
from fping_api import *

time_stamp = time.strftime("%Y-%m-%d %H:%M:%S")

netbox_set = ipv4_address()
fping_set = set()

with open('fping_hosts') as fping:
    for scanned_ini in fping:
        scanned_mod = scanned_ini.rstrip('\n')
        scanned = fping_set.add(scanned_mod + '/32')

for scanned in fping_set:
    if scanned in netbox_set:
        continue
    else:
        ip_add = {"status": "2", "description": "Scanned and marked as alive", "custom_fields": {"Scanned":"1"}, "address": str(scanned)}
        ip_link = 'https://HOSTNAME/api/ipam/ip-addresses/'
        ip_post = requests.post(ip_link, json=ip_add, headers=headers, verify=False)
        log = open('logs/fping_run.log', 'a')
        log_msg = time_stamp + ':' + 'Host:' + str(scanned) + ' has been added.' + '\n'
        log.write(log_msg)
        log.close 
