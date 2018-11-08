import re
import requests
import json
import csv


f = open('/Users/kwolf10/Desktop/PCH/GitHub/katiewolf-pch/JSON_files/saturn.json', 'r')
planet_data = json.load(f)
planet_data = planet_data['docs']

object_urls = []
titles = []

## "object" will give you the link to the actual picture!

for item in planet_data:
	butt = item['isShownAt']
	object_urls.append(butt)
	

for item in planet_data:
	butt = item['sourceResource']['title']
	titles.append(butt)


with open('output.csv', 'w') as results:
	wr = csv.writer(results)
	wr.writerows(zip(object_urls, titles))
