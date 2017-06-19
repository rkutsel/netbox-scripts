import sys, time, re, socket, psycopg2
from db_con import conn, cur, ipam_ip_indx_rst, dcim_iface_indx_rst, dcim_device_indx_rst



#Time stamps for DB updates.
date = time.strftime("%Y-%m-%d")
time_stamp = time.strftime("%Y-%m-%d %H:%M:%S")


def ipam_mgmt_ip():

  #Create "mgmt" network interface for existing devices.
  cur.execute("SELECT id,name FROM dcim_device;")
  for db_fetch in cur.fetchall():

    try:
      ipv4_list = socket.gethostbyname(db_fetch[1])
      #print str(db_fetch[1]) + "<<<" + str(ipv4_list) 
      ipv6_list = socket.getaddrinfo(db_fetch[1], None, socket.AF_INET6)
      #print str(db_fetch[1]) + "<<<" + str(ipv6_list[0][4][0]) 
      #Ignore Loopbacks
      if re.findall(r'127.0.[0-1].1', ipv4_list):
        continue
      cur.execute("INSERT INTO dcim_interface(name, form_factor, mgmt_only, description, device_id) VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING",
                  ("mgmt", "0", "t", db_fetch[1], db_fetch[0]))
      dcim_iface_indx_rst()
      conn.commit()


      cur.execute("SELECT id FROM dcim_interface where name='mgmt' AND device_id=%s;" %(db_fetch[0]))
      iface_id = cur.fetchall()
      cur.execute("SELECT description FROM ipam_ipaddress where description='%s';" %(db_fetch[1]))
      mgmt_ip_desc = cur.fetchall()

      if len(mgmt_ip_desc) == 0:
          #print "Unique Entry"
          cur.execute("INSERT INTO ipam_ipaddress(created, last_updated, family, address, description, interface_id, tenant_id, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT (nat_inside_id) DO NOTHING",
                   (date, time_stamp, "4", ipv4_list, db_fetch[1], iface_id[0], "2", "1"))
          print "Adding:" + str(db_fetch[1]) + "  " + str(ipv4_list)
          ipam_ip_indx_rst()
          cur.execute("INSERT INTO ipam_ipaddress(created, last_updated, family, address, description, interface_id, tenant_id, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT (nat_inside_id) DO NOTHING",
                   (date, time_stamp, "6", ipv6_list[0][4][0], db_fetch[1], iface_id[0], "2", "1"))
          print "Adding:" + str(db_fetch[1]) + "  " + str(ipv6_list[0][4][0])
          ipam_ip_indx_rst()
          conn.commit()
      elif str(mgmt_ip_desc[0][0]) == str(db_fetch[1]):
          print "Hostanme:" +  str(db_fetch[1]) + " " + "already has a management IP" + " >> " + str(ipv4_list) + " >> " + str(ipv6_list[0][4][0])
          continue
      else:
          print "None found. A new DB record is added" + str(uniq_mgmt_ip[0][0])
          cur.execute("INSERT INTO ipam_ipaddress(created, last_updated, family, address, description, interface_id, tenant_id, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT (nat_inside_id) DO NOTHING",
                 (date, time_stamp, "4", ipv4_list, db_fetch[1], int_id[0], "2", "1"))
          cur.execute("INSERT INTO ipam_ipaddress(created, last_updated, family, address, description, interface_id, tenant_id, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT (nat_inside_id) DO NOTHING",
                 (date, time_stamp, "6", ipv6_list[0][4][0], db_fetch[1], int_id[0], "2", "1"))
          ipam_ip_indx_rst()
          conn.commit()
    except socket.gaierror:
      continue


  cur.execute("SELECT id,family,description FROM ipam_ipaddress WHERE family=4;")
  for prim_ip_set in cur.fetchall():
    #print str(prim_ip_set[0]) + str(str(prim_ip_set[1]))
    cur.execute("UPDATE dcim_device SET primary_ip4_id = %s WHERE name=%s", (prim_ip_set[0], prim_ip_set[2]))
    conn.commit()

  cur.execute("SELECT id,family,description FROM ipam_ipaddress WHERE family=6;")
  for prim_ip_set in cur.fetchall():
    #print str(prim_ip_set[0]) + str(str(prim_ip_set[1]))
    cur.execute("UPDATE dcim_device SET primary_ip6_id = %s WHERE name=%s", (prim_ip_set[0], prim_ip_set[2]))
    conn.commit()

ipam_mgmt_ip() 
dcim_device_indx_rst()
