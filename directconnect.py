accountimport os,json,pprint,netaddr
from colorama import Fore,Style
from netaddr import *
from api import *


print(Style.BRIGHT, Fore.CYAN + '\nChoose the environment for the new Direct-Connect\n s\n')
init_input = input(Fore.YELLOW + 'Available options:\n [1] for STAGE \n [2] for PROD\n >>>')

aws_virtual_iface_stage = 'aws --profile STAGE_PROFILE_NAME directconnect describe-virtual-interfaces | grep -v customerRouterConfig\n\n'
aws_virtual_iface_prod = 'aws --profile PROD__PROFILE_NAME directconnect describe-virtual-interfaces | grep -v customerRouterConfig\n\n'
aws_stage_vlans = []
aws_prod_vlans = []

#Upon execution, you are presented with two options:
#If "1" is chosen, then this portion is exectuted.
#note: "1" represents STAGE environment per this example.
if init_input == '1':

    init_stage = json.loads(os.popen(aws_virtual_iface_stage).read())

    for items in init_stage.items():
        #print(Fore.GREEN + json.dumps(items[1], indent=4, sort_keys=True))
        pprint.pprint(items, stream=None, indent=1, width=90, depth=None, compact=True)

    for items in init_stage.items():
        for vlans in items[1]:
            aws_stage_vlans.append(vlans['vlan'])
    #print (max(aws_vlans) + 1)

    while True:
        print(Style.BRIGHT, Fore.CYAN + '\n\n\n' + str(IPNetwork(ipv4_stage()[1]).cidr) + ' will be reserved for the dxcon-11111111 Direct Connect ID\n\n' )
        aws_account_number = input(Fore.YELLOW + 'Enter AWS account number you need to set up Direct Connect with:')
        aws_iface_name = input(Fore.YELLOW + 'Enter AWS Virtual Interface Name (i.e. STAGE_01 - TO - STAGE_02):')
        aws_virtual_iface_create = 'aws --debug --profile STAGE_PROFILE_NAME directconnect allocate-private-virtual-interface --connection-id {} --owner-account {} --new-private-virtual-interface-allocation virtualInterfaceName={},vlan={},asn={},authKey={},amazonAddress={},customerAddress={} | grep -v DEBUG'.format(str('dxcon-11111111'), str(aws_account_number), str(aws_iface_name), str((max(aws_stage_vlans) + 1)), str('11111'), str('bgp' + str(max(aws_vlans) + 1)), str(ipv4_stage()[0]), str(ipv4_stage()[1]))

        if os.popen(aws_virtual_iface_create).read():
            prefix_add = {"description": aws_iface_name, "site": "1", "status": "1", "prefix": str(IPNetwork(ipv4_stage()[0]).cidr)}
            ip_link = 'https://netbox-url.net/api/ipam/prefixes/'
            ip_post = requests.post(ip_link, json=prefix_add, headers=headers)

            print(Style.BRIGHT, Fore.CYAN + '\n\n\n' + str(IPNetwork(ipv4_stage()[1]).cidr) + ' will be reserved for the dxcon-22222222 Direct Connect ID\n\n' )
            aws_account_number = input(Fore.YELLOW + 'Enter AWS account number you need to set up Direct Connect with:')
            aws_iface_name = input(Fore.YELLOW + 'Enter AWS Virtual Interface Name (i.e. STAGE_01 - TO - STAGE_03):')
            aws_virtual_iface_create = 'aws --debug --profile account-test directconnect allocate-private-virtual-interface --connection-id {} --owner-account {} --new-private-virtual-interface-allocation virtualInterfaceName={},vlan={},asn={},authKey={},amazonAddress={},customerAddress={} | grep -v DEBUG'.format(str('dxcon-11111111'), str(aws_account_number), str(aws_iface_name), str((max(aws_stage_vlans) + 2)), str('11111'), str('bgp' + str(max(aws_vlans) + 2)), str(ipv4_stage()[0]), str(ipv4_stage()[1]))

            if os.popen(aws_virtual_iface_create).read():
                prefix_add = {"description": aws_iface_name, "site": "1", "status": "1", "prefix": str(IPNetwork(ipv4_stage()[0]).cidr)}
                ip_link = 'https://netbox-url.net/api/ipam/prefixes/'
                ip_post = requests.post(ip_link, json=prefix_add, headers=headers)
        else: break
        break
#If "2" is chosen then this portion gets exectuted.
#note: "2" represents PROD environment.
else:

    init_prod = json.loads(os.popen(aws_virtual_iface_prod).read())

    for items in init_prod.items():
        #print(Fore.GREEN + json.dumps(items[1], indent=4, sort_keys=True))
        pprint.pprint(items, stream=None, indent=1, width=90, depth=None, compact=True)

    for items in init_prod.items():
        for vlans in items[1]:
            aws_prod_vlans.append(vlans['vlan'])
    #print (max(aws_prod_vlans) + 1)

    while True:
        print(Style.BRIGHT, Fore.CYAN + '\n\n\n' + str(IPNetwork(ipv4_prod()[1]).cidr) + ' will be reserved for the dxcon-11111111 Direct Connect ID\n\n' )
        aws_account_number = input(Fore.YELLOW + 'Enter AWS account number you need to set up Direct Connect with:')
        aws_iface_name = input(Fore.YELLOW + 'Enter AWS Virtual Interface Name (i.e. PROD_01 - TO - PROD_02):')
        aws_virtual_iface_create = 'aws --debug --profile account-prod directconnect allocate-private-virtual-interface --connection-id {} --owner-account {} --new-private-virtual-interface-allocation virtualInterfaceName={},vlan={},asn={},authKey={},amazonAddress={},customerAddress={} | grep -v DEBUG'.format(str('dxcon-11111111'), str(aws_account_number), str(aws_iface_name), str((max(aws_prod_vlans) + 1)), str('11111'), str('bgp' + str(max(aws_prod_vlans) + 1)), str(ipv4_prod()[0]), str(ipv4_prod()[1]))

        if os.popen(aws_virtual_iface_create).read():
            prefix_add = {"description": aws_iface_name, "site": "16", "status": "1", "prefix": str(IPNetwork(ipv4_prod()[0]).cidr)}
            ip_link = 'https://netbox-url.net/api/ipam/prefixes/'
            ip_post = requests.post(ip_link, json=prefix_add, headers=headers)

            print(Style.BRIGHT, Fore.CYAN + '\n\n\n' + str(IPNetwork(ipv4_prod()[1]).cidr) + ' will be reserved for the dxcon-22222222 Direct Connect ID\n\n' )
            aws_account_number = input(Fore.YELLOW + 'Enter AWS account number you need to set up Direct Connect with:')
            aws_iface_name = input(Fore.YELLOW + 'Enter AWS Virtual Interface Name (i.e. PROD_01 - TO - PROD_03):')
            aws_virtual_iface_create = 'aws --debug --profile account-prod directconnect allocate-private-virtual-interface --connection-id {} --owner-account {} --new-private-virtual-interface-allocation virtualInterfaceName={},vlan={},asn={},authKey={},amazonAddress={},customerAddress={} | grep -v DEBUG'.format(str('dxcon-22222222'), str(aws_account_number), str(aws_iface_name), str((max(aws_prod_vlans) + 2)), str('11111'), str('bgp' + str(max(aws_prod_vlans) + 2)), str(ipv4_prod()[0]), str(ipv4_prod()[1]))

            if os.popen(aws_virtual_iface_create).read():
                prefix_add = {"description": aws_iface_name, "site": "1", "status": "1", "prefix": str(IPNetwork(ipv4_prod()[0]).cidr)}
                ip_link = 'https://netbox-url.net/api/ipam/prefixes/'
                ip_post = requests.post(ip_link, json=prefix_add, headers=headers)
        else: break
        break
