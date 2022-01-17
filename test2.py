#!/usr/bin/env python
# This is my btc.py script.

from influxdb import InfluxDBClient
import requests
import datetime



import datetime

x = datetime.datetime.now()


response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
print(data["bpi"]["USD"]["rate"])


# val1 = data["bpi"]
val2 = data["bpi"]["USD"]["rate"]

client = InfluxDBClient('192.168.29.148', 8086, 'admin', 'admin', 'test')

# client.create_database('test')

json_body = [
    {
        "measurement": "test",
        "tags": {
            "host": "server01",
            "region": "us-west",
            "DATE": x,
        },
        "fields": {
            # "value": val1,
            "value1": val2,
            # "DATE": x,
        }
    }
]

client.write_points(json_body)