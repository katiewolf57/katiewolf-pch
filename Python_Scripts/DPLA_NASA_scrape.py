import re
import requests
import json
import csv
import os
import math
import time

## all the planets I will be searching over (including pluto b/c it can still look nice)
planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']

os.mkdir('./planets/')

## DPLA SCRAPING ##

## putting in my API key
keykey = json.load(open('./api.json', 'r'))
dpla_token = keykey['DPLA_token']

# dpla_token = 'YOURKEYHERE'

## making an empty list so I can fill it with all my search results
dpla_all_data = []

## page size is 500 and there are NOT more than 500 results for each planet --> don't have to loop through multiple pages
for planet in planets:

	## making a directory to store files/images in
	if not os.path.exists('./planets/' + planet):
		os.mkdir('./planets/' + planet)

	print("Looking at " + planet + ' in DPLA!\n')
	payload = {'q': 'planet+AND+' + planet, 'page_size':500,'sourceResource.type':'image', 'api_key': dpla_token}
	r = requests.get('https://api.dp.la/v2/items', params = payload)

	dpla_data = json.loads(r.text)
	## adding the search results for this planet to my results list
	dpla_all_data.append(dpla_data)

	## writing out the data for each planet it it's own JSON file for easier searching
	## adding it to the planet folder
	json.dump(dpla_data, open('./planets/' + planet + '/' + planet + '_dpla.json', 'w'), indent=4)


	print("Made a " + planet + " JSON file\n")



json.dump(dpla_all_data, open('./planets/dpla_data.json', 'w'), indent=4)



## NASA SCRAPING ##

## where I'm putting all the data ##
nasa_all_data = []

## where I'm putting planet data (clears after each planet loop) ##
planet_data = []

for planet in planets:

	## looping through pages for this search ##
    page = 1

    print('Looking at ' + planet + ' in NASA!\n')
    payload = {'q': planet, 'media_type': 'image', 'page': page}
    r = requests.get('https://images-api.nasa.gov/search', params=payload)

    nasa_data = json.loads(r.text)

	## need to determine how many pages to loop through for each plaent##
    total_hits = nasa_data['collection']['metadata']['total_hits']

	## how many hits are there ##
	## 100 hits per page -> hits/100 = pages needed ##
    total_pages = math.ceil(total_hits/100)


	## if LESS THAN 100 pages needed, then no problem ##
    if total_pages <=100:
        while page <= total_pages:
            payload = {'q': planet, 'media_type': 'image', 'page': page}
            r = requests.get('https://images-api.nasa.gov/search', params=payload)

            nasa_data = json.loads(r.text)

            planet_data.append(nasa_data)
            nasa_all_data.append(nasa_data)
            print('Finished ' + planet + ' page ' + str(page))

            page = page + 1

        json.dump(planet_data, open('./planets/' + planet + '/' + planet + '_nasa.json', 'w'), indent = 4)
        print('Made a ' + planet + ' JSON file\n')

        planet_data.clear()


	## it won't let me load more than 100 pages per search ##
	## making sure that planets (earth and mars) with more than 100 pages don't exceed that limit ##
    else:
        while page <= 100:
            payload = {'q': planet, 'media_type': 'image', 'page': page}
            r = requests.get('https://images-api.nasa.gov/search', params=payload)

            nasa_data = json.loads(r.text)

            planet_data.append(nasa_data)
            nasa_all_data.append(nasa_data)
            print('Finished ' + planet + ' page ' + str(page))

            page = page + 1

            json.dump(planet_data, open('./planets/' + planet + '/' + planet + '_nasa.json', 'w'), indent = 4)

        print('Made a ' + planet + ' JSON file\n')

        planet_data.clear()

json.dump(nasa_all_data, open('./planets/nasa_data.json', 'w'), indent=4)
