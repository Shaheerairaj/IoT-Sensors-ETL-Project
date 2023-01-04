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

col_names = ['DataMessageGUID','SensorID','MessageData','State','SignalStrength','Voltage','Battery',
'Data','DisplayData','PlotValue','MetNotificationRequirements','GatewayID','DataValues','DataTypes',
'PlotValues','PlotLabels']

df = pd.DataFrame()
sensor_list = sensor_list[:5]    # Limiter for testing

try:

    for i in sensor_list:

        data_message_params = {
            'sensorID':sensor_list[i],
            'fromDate':fromDate,
            'toDate'  :toDate
        }

        logging.info("Calling sensor data")
        r = requests.post(data_message_URL, params=data_message_params, headers=headers, verify=False)
        logging.info(r.status_code)
        data = r.json()

        df_r = pd.DataFrame(data['Result'], index=[0])
        df_r['Sensor Name'] = sensor_name[i]
        df_r['MessageDate'] = int(df_r['MessageDate'].str[6:-2]) / 1000
        df_r['MessageDate'] = (datetime.datetime.fromtimestamp(df_r['MessageDate'])).strftime("%Y-%m-%d %H:%M:%S")

        df.append(df_r)

except:
    logging.info(f"Ran into error while calling data messages at {sensor_name[i]}")



print(df.head())