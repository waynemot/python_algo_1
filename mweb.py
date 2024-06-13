import pickle
import os
#import pyodbc
#import mariadb
import pymysql.cursors
#from config import config

# Environment vars inspection
#for a in os.environ:
#    print('Var: ', a, 'Value: ', os.getenv(a))

uname = os.environ.get("USER")
pw = os.environ.get("PASS")
#host = 'cse-cosmos-1.unl.edu'
host = 'localhost'
driver = "MariaDB ODBC 3.1 Driver"
#database = 'usgs_crns_corr_production'
database='wmotycka'

print("user: "+uname);
print("pass: "+pw);

#query = 'SELECT login, nuid FROM view_login_nuid where nuid in (\'35140602\')'
#query = 'SELECT * FROM view_login_nuid limit 1'
#query = "SELECT * FROM sites WHERE removal_date is null LIMIT 2"
query = "SELECT * FROM sites"

print(query)
#                 "charset=utf8mb4;")%(
#                "Trusted_Connection = yes;")%(
#connStr = ("Driver=%s;" "Server = %s;" "Database = %s;" "uid = %s;" "password = %s;" )%( config.udb.driver, config.udb.host, config.udb.database, config.udb.username, config.udb.password)
#connStr = ("Driver=%s;" "Server=%s;" "Database=%s;" "uid=%s;" "password='%s';" )%( driver, host, database, uname, pw)
connStr = {"user":uname, "password":pw, "host":'localhost', 'database':'usgs_crns_production'}
pymyStr = {"user":uname, "password":pw, "host":'localhost', 'database':'usgs_crns_production', 'charset':'utf8mb4', 'cursorclass':pymysql.cursors.DictCursor}
try:
  #conn = pyodbc.connect(connStr)
  #conn = mariadb.connect(**connStr)
  conn = pymysql.connect(**pymyStr)
  #conn.setencoding(encoding='utf-8')
  #conn.setencoding('utf-8')
  #conn.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8', ctype=pyodbc.SQL_CHAR)
  #conn.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8', ctype=pyodbc.SQL_WCHAR)
  #conn.setdecoding(pyodbc.SQL_WCHAR, encoding='ansi', ctype=pyodbc.SQL_WCHAR)
  #tried: https://stackoverflow.com/questions/29458260/python-pyodbc-unicode-issue
  #conn.setdecoding(pyodbc.SQL_CHAR, encoding='iso-8859-1')
  #conn.setdecoding(pyodbc.SQL_WCHAR, encoding='iso-8859-1')
  #conn.setencoding(encoding='iso-8859-1')
  cursor = conn.cursor()
  cursor.execute(query)
  #result = cursor.fetchone()
  #print result
  for row in cursor:
    #(id, name, site_id, created_at, updated_at, installation, customer, number, irid_imei_number, description, n1_n0, n2_n0, n3_n0, center_latitude, center_longitude, elevation, timezone, cutoff_rigidity, mean_pressure, mean_water_vapor, bulk_density, lattice_water, soil_organic_carbon, bio_mass, installation_date, removal_date, has_gps_data, last_date, calibrated, selected, status, network_affiliation, algorithm, entity, short_name, station_id )
    print(*row, sep=' ')
   # (login,nuid) = row
   # print(site_id)
   # print(name)
#except mariadb.Error as e:
except pymysql.Error as e:
  print("unable to connect/query db")
  print(e)

