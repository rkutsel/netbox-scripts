## ipam_mgmt.py 
  The script attmepts to resolve each hostname in netbox DB then creates a **"mgmt"** interface with its corresponding IPv4/IPv6 addresses. 		  The script attmepts to resolve each hostname in netbox DB then creates a **"mgmt"** interface with its corresponding IPv4/IPv6 addresses. 
 +
 +## fping_prefixes.py
 +Makes an API call to NetBox and returns the list of IPv4 prefixes, then saves the list of returned prefixes to **fping_prefixes file**. 
 +
 +## fping.sh
 +Runs fping against each subnet found in **fping_prefixes** file and saves "Alive" hosts in **fping_hosts** file. 
 +
 +## fping.sh
 +Adds unique entries found **fping_hosts** file and ultimately adds them to NetBox. 
 +
