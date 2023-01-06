import mysql.connector
import pandas as pd

df = pd.read_excel('Sensor data.xlsx')
df = df.iloc[0:5]

# Connect to MySQL server and run a query (create a test database)

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='QwertyLayout'
)

mycursor = db.cursor()

# Creating column list for insertion
cols = "`,`".join([str(i) for i in df.columns.tolist()])

# Inserting DataFrame records
for i, row in df.iterrows():
    sql = "INSERT INTO `vibration_sensor` (`" + cols +"`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
    mycursor.execute(sql, tuple(row))