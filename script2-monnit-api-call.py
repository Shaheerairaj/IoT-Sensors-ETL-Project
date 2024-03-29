import pandas as pd
import requests
import datetime
import logging
import warnings
warnings.filterwarnings("ignore")

logging.basicConfig(filename='script2-monnit-api-call.log', level=logging.INFO,
format='%(asctime)s:%(levelname)s:%(message)s')

scriptStartTime = datetime.datetime.now()

sensor_list_URL = 'https://www.imonnit.com/json/SensorList'
data_message_URL= 'https://www.imonnit.com/json/SensorDataMessages'

headers = {
    'APIKeyID':'d6MFjHhdC3RX',
    'APISecretKey': 'rAOioqNQvnkmISoMDJ1FjjIvS282AYwz'
}

try:
    logging.info("Calling sensor list API")
    r = requests.post(sensor_list_URL, headers=headers, verify=False)
    logging.info(r.status_code)
    data = r.json()

except:
    logging.info("Ran into error when calling sensor list end point")




sensor_list = []
sensor_name = []

for sensorID in range(0, len(data['Result'])):

    sensor_list.append(data['Result'][sensorID]['SensorID'])
    sensor_name.append(data['Result'][sensorID]['SensorName'])





fromDate = (datetime.datetime.now() - datetime.timedelta(hours=6)).strftime("%m/%d/%Y %H:00:00")
toDate   = (datetime.datetime.now() - datetime.timedelta(hours=5)).strftime("%m/%d/%Y %H:00:00")

df = pd.DataFrame()

logging.info("Calling sensor data for all sensors")

try:

    for i in range(0,len(sensor_list)):

        data_message_params = {
            'sensorID':sensor_list[i],
            'fromDate':fromDate,
            'toDate'  :toDate
        }

        r = requests.post(data_message_URL, params=data_message_params, headers=headers, verify=False)
        data = r.json()

        index_range = list(range(0,len(data['Result'])))

        df_r = pd.DataFrame(data['Result'], index=index_range)
        df_r['SensorType'] = sensor_name[i]

        df = df.append(df_r)

except:
    logging.info(f"Ran into error while calling data messages at {sensor_name[i]}")
    logging.info(r.status_code)



# Final Transformations
df.reset_index(inplace=True, drop=True)
df['MessageDate'] = df['MessageDate'].str[6:-2]
df['DataTimeStamp'] = df['MessageDate'].apply(lambda x: datetime.datetime.fromtimestamp(int(x)/1000).strftime("%Y-%m-%d %H:%M:%S"))

df.rename(columns={'Data':'RawData'}, inplace=True)
df['MessageDate'] = df['MessageDate'].astype(float)

new = df['SensorType'].str.split(' - ', expand=True)
df['SensorType'] = new[0]




scriptEndTime = datetime.datetime.now()
scriptRunningTime = scriptEndTime - scriptStartTime
logging.info(f"Time taken to run script: {scriptRunningTime}")


df.to_excel('Sensor data.xlsx', index=False)