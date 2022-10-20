from flask import Flask, render_template
import ibm_db;

app = Flask(__name__)

dsn_hostname = "3883e7e4-18f5-4afe-be8c-fa31c41761d2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
dsn_uid = "ghc72736"
dsn_pwd = "uz905NueevL1upTM"

dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "BLUDB"
dsn_port = "50000"
dsn_protocol = "TCPIP"

dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};"
).format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd)

print(dsn)

try:
    conn = ibm_db.connect(dsn, "", "")
    print("Connected to database: ", dsn_database, " as user: ", dsn_uid, " on host: ", dsn_hostname)
except:
    print("Unable to connect: ", ibm_db.conn_errormsg())

@app.route("/sign-up")
def hello_world():
    return render_template('register.html')

@app.route("/sign-in")
def toSignUpPage():
    return render_template('signin.html')

@app.route("/")
def toHomePage():
    return render_template('home.html')  


