import ibm_db
import sys
def get_connection():

hostname="2f3279a5-73d1-4859-88f0-a6c3e6b4b907.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud"
uid="vkh98069"
pwd="w7F7JbCb00H3Y4uz"
driver="{IBM DB2 ODBC DRIVER}"
db="blud"
port="30756"
protocol="TCPIP"
cert="certificate.crt"

dsn=(
     "DATABASE={0};"
     "HOSTNAME={1};"
     "PORT={2};"
     "UID={3};"
     "SECURITY=SSL;"
     "SSLServerCertificate={4};"
     "PWD={5};"
     ).format(db,hostname,port,uid,cert,pwd)
print(dsn)
try:
    db2=ibm_db.connect(dsn,"","")
    print("Connected to database")
except:
    print("unable to connect",ibm_db.conn_errormsg())
    sys.exit(1)
get_connection()
