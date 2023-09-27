import pickle
import os.path
import pyodbc
from config import config

#query = 'SELECT login, nuid FROM view_login_nuid where nuid in (\'35140602\')'
query = 'SELECT login FROM view_login_nuid limit 1'

print(query)
#                 "charset=utf8mb4;")%(
#                "Trusted_Connection = yes;")%(
connStr = ("Driver=%s;" "Server = %s;" "Database = %s;" "uid = %s;" "password = %s;" )%( config.udb.driver, config.udb.host, config.udb.database, config.udb.username, config.udb.password)
try:
  conn = pyodbc.connect(connStr)
  #conn.setencoding(encoding='utf-8')
  #conn.setencoding('utf-8')
  #conn.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8', ctype=pyodbc.SQL_CHAR)
  conn.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8', ctype=pyodbc.SQL_WCHAR)
  #conn.setdecoding(pyodbc.SQL_WCHAR, encoding='ansi', ctype=pyodbc.SQL_WCHAR)
  #tried: https://stackoverflow.com/questions/29458260/python-pyodbc-unicode-issue
  #conn.setdecoding(pyodbc.SQL_CHAR, encoding='iso-8859-1')
  #conn.setdecoding(pyodbc.SQL_WCHAR, encoding='iso-8859-1')
  #conn.setencoding(encoding='iso-8859-1')
  cursor = conn.cursor()
  cursor.execute(query)
#  for row in cursor:
#    (login,nuid) = row
#    print(login)
#    print(nuid)
except pyodbc.Error as e:
  print("unable to connect to db")
  print(e)

