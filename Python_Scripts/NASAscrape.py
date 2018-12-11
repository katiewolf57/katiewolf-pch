import re
import requests
import json
import csv
import os
import math

nasa_all_data = []
planet_data = []

planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
for planet in planets:
    page = 1

    print('Looking at ' + planet)
    payload = {'q': planet, 'media_type': 'image', 'page': page}
    r = requests.get('https://images-api.nasa.gov/search', params=payload)

    nasa_data = json.loads(r.text)

    total_hits = nasa_data['collection']['metadata']['total_hits']
    print(total_hits)
    total_pages = math.ceil(total_hits/100)
    print(total_pages)

    if total_pages <=100:
        while page <= total_pages:
            payload = {'q': planet, 'media_type': 'image', 'page': page}
            r = requests.get('https://images-api.nasa.gov/search', params=payload)

            nasa_data = json.loads(r.text)

            planet_data.append(nasa_data)
            nasa_all_data.append(nasa_data)
            print('Finished ' + planet + ' page ' + str(page))

            page = page + 1

        json.dump(planet_data, open(planet + '.json', 'w'), indent = 4)
        print('Made a ' + planet + ' JSON file\n')

        planet_data.clear()

    else:
        while page <= 100:
            payload = {'q': planet, 'media_type': 'image', 'page': page}
            r = requests.get('https://images-api.nasa.gov/search', params=payload)

            nasa_data = json.loads(r.text)

            planet_data.append(nasa_data)
            nasa_all_data.append(nasa_data)
            print('Finished ' + planet + ' page ' + str(page))

            page = page + 1

    if total_pages > 100:
        page = 100
        while page <= total_pages:
            payload = {'q': planet, 'media_type': 'image', 'page': page}
            r = requests.get('https://images-api.nasa.gov/search', params=payload)

            nasa_data = json.loads(r.text)

            planet_data.append(nasa_data)
            nasa_all_data.append(nasa_data)
            print('Finished ' + planet + ' page ' + str(page))

            page = page + 1

        json.dump(planet_data, open(planet + '.json', 'w'), indent = 4)
        print('Made a ' + planet + ' JSON file\n')

        planet_data.clear()
