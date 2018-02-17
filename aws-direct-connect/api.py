import sys,time,requests,json
from netaddr import *


#NetBox API Token
headers = {'Authorization': 'Token YOUR_API_TOKEN'}

def ipv4_stage():
#NetBox API call to retreive test prefix 169.254.0.0/20 list.
    stage_supernet = '169.254.0.0/20'
    stage_set = set()
    api_link = 'https://netbox-url.net/api/ipam/prefixes/?parent=169.254.0.0/20&status=1'
    api_init = requests.get(api_link, headers=headers)
    s_list = json.loads(api_init.text)
    for prefixes in s_list[u'results']:
        #print(prefixes[u'prefix'])
        stage_set.add(prefixes[u'prefix'])
    if stage_supernet in stage_set: stage_set.remove(stage_supernet)
    ipv4_addr_space = IPSet(['169.254.0.0/20'])
    available = ipv4_addr_space ^ IPSet(stage_set)
    AWS_peer_ip = list(available)[1]
    S_peer_ip = list(available)[2]
    bgp_peers = [str(AWS_peer_ip) + '/30', str(S_peer_ip) + '/30']
    return bgp_peers

def ipv4_prod():
#Initial API call to retreive production 169.254.16.0/23 subnets.
    prod_supernet = '169.254.16.0/20'
    prod_set = set()
    api_link = 'https://netbox-url.net/api/ipam/prefixes/?parent=169.254.16.0/20&status=1'
    api_init = requests.get(api_link, headers=headers)
    p_list = json.loads(api_init.text)
    for prefixes in p_list[u'results']:
        #print(prefixes[u'prefix'])
        prod_set.add(prefixes[u'prefix'])
    if prod_supernet in prod_set: prod_set.remove(prod_supernet)
    ipv4_addr_space = IPSet(['169.254.16.0/20'])
    available = ipv4_addr_space ^ IPSet(prod_set)
    AWS_peer_ip = list(available)[1]
    P_peer_ip = list(available)[2]
    bgp_peers = [str(AWS_peer_ip) + '/30', str(P_peer_ip) + '/30']
    return bgp_peers
