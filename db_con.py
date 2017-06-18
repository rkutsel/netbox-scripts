import psycopg2
conn = psycopg2.connect("dbname='netbox' user='netbox' host='localhost' password=''")
cur = conn.cursor()
