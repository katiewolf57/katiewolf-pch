import re
import requests
import json
import csv
import os


## putting in my API key
# keykey = json.load(open('/Users/kwolf10/Desktop/PCH/GitHub/katiewolf-pch/JSON_files/api.json', 'r'))
dpla_token = 'eaf8cfe93ba9d5f249ba85073fbb7ebd'

print (dpla_token)

## making an empty list so I can fill it with all my search results
dpla_all_data = []
## all the planets I will be searching over (including pluto b/c it can still look nice)
planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']


## looping through my planet list
## page size is 500 and there are NOT more than 500 results for each planet --> don't have to loop through multiple pages

for planet in planets:

	## making a directory to store files/images in
	os.mkdir(planet)

	print("Looking at " + planet + '!\n')
	payload = {'q': 'planet+AND+' + planet, 'page_size':500,'sourceResource.type':'image', 'api_key': dpla_token}
	r = requests.get('https://api.dp.la/v2/items', params = payload)

	dpla_data = json.loads(r.text)
	## adding the search results for this planet to my results list
	dpla_all_data.append(dpla_data)

	## writing out the data for each planet it it's own JSON file for easier searching
	## adding it to the planet folder
	json.dump(dpla_data, open('./' + planet + '/' + planet + '_dpla' + '.json', 'w'), indent=4)


	print("Made a " + planet + " JSON file\n")



json.dump(dpla_all_data, open('dpla_data.json', 'w'), indent=4)
