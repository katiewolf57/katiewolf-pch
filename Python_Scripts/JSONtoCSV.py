import re
import requests
import json
import csv


f = open('uranus.json', 'r')
planet_data = json.load(f)
planet_data = planet_data['docs']

data = []

for item in planet_data:
	butt = item['sourceResource']
	data.append(butt)
	

json.dump(data, open('testing.json', 'w'), indent=4)
