import psycopg2
conn = psycopg2.connect("dbname='netbox' user='netbox' host='localhost' password=''")
cur = conn.cursor()



#Reset dcim_device_sequence DB index
def dcim_device_indx_rst():
  if cur.execute("SELECT MAX(id) FROM dcim_device") == 0:
    cur.execute("ALTER SEQUENCE dcim_device_id_seq RESTART WITH 1")
    conn.commit()
    #quit()
  else:
    cur.execute("ALTER SEQUENCE dcim_device_id_seq RESTART with %s" %(int(cur.fetchall()[0][0] + 1)))
    conn.commit()
  return



#Reset dcim_devicetype_sequence DB index
def dcim_devicetype_indx_rst():
  if cur.execute("SELECT MAX(id) FROM dcim_devicetype")  == 0:
    cur.execute("ALTER SEQUENCE dcim_devicetype_id_seq RESTART WITH 1")
    conn.commit()
    #quit()
  else:
    cur.execute("ALTER SEQUENCE dcim_devicetype_id_seq RESTART with %s" %(cur.fetchall()[0][0] + 1))
    conn.commit()
  return


#Reset dcim_platform_sequence DB index
def dcim_platform_indx_rst():
  if cur.execute("SELECT MAX(id) FROM dcim_platform")  == 0 or cur.execute("SELECT MAX(id) FROM dcim_platform")  is None:
    cur.execute("ALTER SEQUENCE dcim_platform_id_seq RESTART WITH 1")
    conn.commit()
    #quit()
  else:
    cur.execute("ALTER SEQUENCE dcim_platform_id_seq RESTART with %s" %(cur.fetchall()[0][0] + 1))
    conn.commit()
  return


#Reset dcim_interface_id_seq DB index
def dcim_iface_indx_rst():
  if cur.execute("SELECT MAX(id) FROM dcim_interface") == 0:
    cur.execute("ALTER SEQUENCE dcim_interface_id_seq RESTART WITH 1")
    conn.commit()
    #quit()
  else:
    cur.execute("ALTER SEQUENCE dcim_interface_id_seq RESTART with %s" %(int(cur.fetchall()[0][0] + 1)))
    conn.commit()
  return


#Reset ipam_ipaddress_id_seq DB index
def ipam_ip_indx_rst():
  if cur.execute("SELECT MAX(id) FROM ipam_ipaddress") == 0:
    cur.execute("ALTER SEQUENCE ipam_ipaddress_id_seq RESTART WITH 1")
    conn.commit()
    #quit()
  else:
    cur.execute("ALTER SEQUENCE ipam_ipaddress_id_seq RESTART with %s" %(int(cur.fetchall()[0][0] + 1)))
    conn.commit()
  return
