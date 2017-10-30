import sys, time
import requests, json


#NetBox API Token
headers = {'Authorization': 'YOUR TOKEN'}


def ipv4_prefix():
#Prefix list API. Initial API call to retreive first batch.
    prefix_list = []
    api_init = "https://HOSTNAME/api/ipam/prefixes/?status=1&family=4"
    api_prefixes = requests.get(api_init, headers=headers, verify=False)
    z_prefixes = json.loads(api_prefixes.text)
    for prefixes in z_prefixes[u'results']:
        prefix_list.append(prefixes[u'prefix'])

#Prefix list API. Sebsequent API request(s) due to API pagination. The default MAX is value "?limit=1000"
    for subsequent in z_prefixes[u'next']:
        if z_prefixes[u'next']:
            http_req_prefixes = requests.get(z_prefixes[u'next'], headers=headers, verify=False)
            z_prefixes = json.loads(http_req_prefixes.text)
            for prefixes in z_prefixes[u'results']:
                #print prefixes[u'prefix']
                prefix_list.append(prefixes[u'prefix'])
    return prefix_list




def ipv4_address():
#Initial API call to retreive first batch.
    ip_set = set()
    api_link = "https://HOSTNAME/api/ipam/ip-addresses/?limit=1000&family=4"
    api_init = requests.get(api_link, headers=headers, verify=False)
    z_ip = json.loads(api_init.text)
    for ips in z_ip[u'results']:
        #print ips[u'address']
        ip_set.add(ips[u'address'])
    for subsequent in z_ip[u'next']:
        if z_ip[u'next']:
            http_req_prefixes = requests.get(z_ip[u'next'], headers=headers, verify=False)
            z_ip = json.loads(http_req_prefixes.text)
            for subsequent in z_ip[u'results']:
                #print subsequent[u'address']
                ip_set.add(subsequent[u'address'])
    return ip_set
 
