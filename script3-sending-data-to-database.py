import mysql.connector
import pandas as pd

df = pd.read_excel('Sensor data.xlsx')
# df = df.iloc[0:5]                       # Limiter for testing

sensor_tables = {
    'Advanced Vibration':'vibration',
    'AirSpeed':'air_speed',
    'Air Quality':'air_quality',
    'CO2 Meter':'co2',
    'CO Meter':'co',
    'Differential Pressure':'diff_press',
    'Duct Temperature':'duct_temp',
    'Humidity':'humidity',
    'LightSensor':'light',
    'PIR ALTA':'motion',
    'Quad Temperature':'quad_temp',
    'Temperature':'temp'
}

# Connect to MySQL server and run a query (create a test database)

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='QwertyLayout',
    db='monnit_iot_sensors'
)

mycursor = db.cursor()

# Creating column list for insertion
cols = "`,`".join([str(i) for i in df.columns.tolist()])


# Filtering df fr sensor type

for sensorType in df['SensorType'].unique():

    df_filtered = df[df['SensorType'] == sensorType]

    # Inserting DataFrame records
    for i, row in df_filtered.iterrows():
        sql = "INSERT INTO `"+ sensor_tables[sensorType] + "` (`" + cols +"`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
        mycursor.execute(sql, tuple(row))

        db.commit()

db.close()