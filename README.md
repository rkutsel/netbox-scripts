# NetBox custom scripts (Python 2.7)
This is an attempt to share some of my work with the [NetBox](https://github.com/digitalocean/netbox) community. I plan on adding more scripts later on.
# Dependencies
Make sure you have all dependencies installed i.e.  
```
$sudo pip install sys, time, re, socket, psycopg2
```
If you don't have pip installed then follow this [guide](https://pip.pypa.io/en/stable/installing/) 
# Installation
Clone the repository and modify **db_con.py** file with your DB information i.e.
```python
import psycopg2
conn = psycopg2.connect("dbname='YOUR_NETBOX_DB_NAME' user='YOUR_NETBOX_USERNAME' host='YOUR_NETBOX_DB_IP_ADDRESS' password='YOUR_NETBOX_DB_PASSWORD'")
cur = conn.cursor()
```

## ipam_mgmt.py 
The script attmepts to resolve each hostname in netbox DB then creates a **"mgmt"** interface with its corresponding IPv4/IPv6 addresses. 
