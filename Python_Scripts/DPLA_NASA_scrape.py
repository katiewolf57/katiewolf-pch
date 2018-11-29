import re
import requests
import json
import csv
import os
import math
import time

## all the planets I will be searching over (including pluto b/c it can still look nice)
planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']

## DPLA SCRAPING ##

## putting in my API key
keykey = json.load(open('/Users/kwolf10/Desktop/PCH/GitHub/katiewolf-pch/JSON_files/api.json', 'r'))

dpla_token = keykey['DPLA_token']
print(dpla_token)

## making an empty list so I can fill it with all my search results
dpla_all_data = []




## page size is 500 and there are NOT more than 500 results for each planet --> don't have to loop through multiple pages
for planet in planets:

	## making a directory to store files/images in
	if not os.path.exists('./' + planet):
		os.mkdir(planet)

	print("Looking at " + planet + ' in DPLA!\n')
	payload = {'q': 'planet+AND+' + planet, 'page_size':500,'sourceResource.type':'image', 'api_key': dpla_token}
	r = requests.get('https://api.dp.la/v2/items', params = payload)

	dpla_data = json.loads(r.text)
	## adding the search results for this planet to my results list
	dpla_all_data.append(dpla_data)

	## writing out the data for each planet it it's own JSON file for easier searching
	## adding it to the planet folder
	json.dump(dpla_data, open('./' + planet + '/' + planet + '_dpla.json', 'w'), indent=4)


	print("Made a " + planet + " JSON file\n")



json.dump(dpla_all_data, open('dpla_data.json', 'w'), indent=4)



## NASA SCRAPING ##

nasa_all_data = []


for planet in planets:

	## results span more than one page for this one ##
	## have to loop through the pages ##
    ## start at page one ## 
    page = 1

    ## where the data will go for each planet ##
    planet_data = []


    print('Looking at ' + planet + ' in NASA!\n')

    payload = {'q': planet, 'media_type':'image', 'page': page}
    r = requests.get('https://images-api.nasa.gov/search', params=payload)
    
    print(payload)
    print(r.text)

    nasa_data = json.loads(r.text)

    ## adding up how many pages are needed: total hits, rounded up, and then divided by 100 (total items per page)
    total_hits = nasa_data['collection']['metadata']['total_hits']
    total_pages = math.ceil(total_hits / 100)
    print(f'There are {total_hits} hits meaning there should be {total_pages} pages.')


    while page <= total_pages:
        

        payload = {'q': 'planet' + planet, 'media_type':'image', 'page': page}
        r = requests.get('https://images-api.nasa.gov/search', params=payload)


        nasa_data = json.loads(r.text)

        # add  in the data
        planet_data.append(nasa_data)

        page = page + 1


    json.dump(planet_data, open('./' + planet + '/' + planet + '_nasa.json', 'w'), indent=4)
    print("Made a " + planet + " JSON file\n")

    time.sleep(10)

    nasa_all_data.append(nasa_data)

json.dump(nasa_all_data, open('nasadata.json', 'w'), indent=4) 
