import re
import requests
import json
import csv
import os


planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']


hrefs = []

## opening up the JSON file to search through for relevant info
f = open('./venus/venus_nasa.json', 'r')
planet_data = json.load(f)
planet_data = planet_data[1]['collection']['items']



for object in planet_data:
    links = object['links']
    for ref in links:
        href=ref['href']
        hrefs.append(href)

count = str(len(hrefs))
print(count)

json.dump(planet_data, open('nasa_test.json', 'w'), indent=4)
