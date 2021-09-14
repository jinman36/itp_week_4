# ITP Week 4 Day 1 Exercise


import requests
import json
import openpyxl
from openpyxl.styles import Font

response = requests.get("https://data.messari.io/api/v2/assets")
# https://data.messari.io/api/v2/assets

clean_data = json.loads(response.text)
symbol_result = clean_data['data'][0]['symbol']
roi_result = clean_data['data'][0]['metrics']['roi_data']

counter = 0

for index in clean_data:
    symbol_list = clean_data['data'][counter]['symbol']
    counter += 1

print(symbol_list)


# print(symbol_result)
# print(roi_result)