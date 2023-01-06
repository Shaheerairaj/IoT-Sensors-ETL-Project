import mysql.connector

# Connect to MySQL server and run a query (create a test database)

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='QwertyLayout'
)

mycursor = db.cursor()

mycursor.execute("CREATE DATABASE testdatabase")