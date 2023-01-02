import pandas as pd
import requests
import datetime

sensor_list_URL = 'https://www.imonnit.com/json/SensorList'
data_message_URL= 'https://www.imonnit.com/json/SensorDataMessages'

headers = {
    'APIKeyID':'d6MFjHhdC3RX',
    'APISecretKey': 'rAOioqNQvnkmISoMDJ1FjjIvS282AYwz'
}

r = requests.post(sensor_list_URL, headers=headers, verify=False)

data = r.json()

print(data['Result'])

sensor_list = []

for i in range(0, len(data['Result'])):

    sensor_list.append(data['Result'][i]['SensorID'])

print(sensor_list)



fromDate = (datetime.datetime.now() - datetime.timedelta(hours=6)).strftime("%m/%d/%Y %H:00:00")
toDate   = (datetime.datetime.now() - datetime.timedelta(hours=5)).strftime("%m/%d/%Y %H:00:00")

print(fromDate)
print(toDate)

data_message_params = {
    'sensorID':sensor_list[0],
    'fromDate':fromDate,
    'toDate'  :toDate
}

r = requests.post(data_message_URL, params=data_message_params, headers=headers, verify=False)
data = r.json()
print(data)

df = pd.DataFrame(data['Result'], index=[0])
df['MessageDate'] = int(df['MessageDate'].str[6:-2]) / 1000
df['MessageDate'] = (datetime.datetime.fromtimestamp(df['MessageDate'])).strftime("%Y-%m-%d %H:%M:%S")

print(df.columns)