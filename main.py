import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS, WriteOptions
import datetime
now = datetime.datetime.now()
from urllib.request import urlopen

import json

url = "https://api.coingecko.com/api/v3/exchange_rates"

response = urlopen(url)

data_json = json.loads(response.read())

print(data_json['rates']['usd'])

token = "ZI3DnutdWQeFmNGRER7B-KA28e_sVNDzivB6JVwpqMFBmLC-WpITPmnHeboAxxpapCZMtvZuxg2txweE0y8WIA=="
org = "uiuc"
url = "http://20.247.104.158:8086"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

bucket = "insertTest"

write_api = client.write_api(write_options=SYNCHRONOUS)

write_api.write(bucket=bucket, org="uiuc", record=[
    {"measurement": data_json['rates']['usd']['name'], "tags": {"unit": data_json['rates']['usd']['unit']}, "fields": {"type": data_json['rates']['usd']['type']},
     "time": now, "value": data_json['rates']['usd']['value']}])