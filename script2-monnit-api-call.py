import pandas as pd
import requests
import datetime
import logging

logging.basicConfig(filename='script2-monnit-api-call.log', level=logging.INFO,
format='%(asctime)s:%(levelname)s:%(message)s')



sensor_list_URL = 'https://www.imonnit.com/json/SensorList'
data_message_URL= 'https://www.imonnit.com/json/SensorDataMessages'

headers = {
    'APIKeyID':'d6MFjHhdC3RX',
    'APISecretKey': 'rAOioqNQvnkmISoMDJ1FjjIvS282AYwz'
}


logging.info("Calling sensor list API")
r = requests.post(sensor_list_URL, headers=headers, verify=False)
logging.info(r.status_code)
data = r.json()




sensor_list = []
sensor_name = []

for sensorID in range(0, len(data['Result'])):

    sensor_list.append(data['Result'][sensorID]['SensorID'])
    sensor_name.append(data['Result'][sensorID]['SensorName'])




fromDate = (datetime.datetime.now() - datetime.timedelta(hours=6)).strftime("%m/%d/%Y %H:00:00")
toDate   = (datetime.datetime.now() - datetime.timedelta(hours=5)).strftime("%m/%d/%Y %H:00:00")

data_message_params = {
    'sensorID':sensor_list[0],
    'fromDate':fromDate,
    'toDate'  :toDate
}

logging.info("Calling sensor data")
r = requests.post(data_message_URL, params=data_message_params, headers=headers, verify=False)
logging.info(r.status_code)
data = r.json()

df = pd.DataFrame(data['Result'], index=[0])
df['MessageDate'] = int(df['MessageDate'].str[6:-2]) / 1000
df['MessageDate'] = (datetime.datetime.fromtimestamp(df['MessageDate'])).strftime("%Y-%m-%d %H:%M:%S")

print(df.columns)

# Complete logging
# Add sensor name to df
# Exception handling when calling API
# For loop to call data for all sensors