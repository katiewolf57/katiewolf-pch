import re
import requests
import json
import csv


## putting in my API key
dpla_token = json.load(open('api.json', 'r'))
dpla_token = dpla_token['DPLA_Token']

## making an empty list so I can fill it with all my search results
dpla_all_data = []
## all the planets I will be searching over (including pluto b/c it can still look nice)
planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']


## looping through my planet list
## page size is 500 and there are NOT more than 500 results for each planet --> don't have to loop through multiple pages

# for planet in planets:
# 	payload = {'q': 'planet+AND+' + planet, 'page_size':500, 'api_key': dpla_token}
# 	r = requests.get('https://api.dp.la/v2/items', params = payload)

# 	dpla_data = json.loads(r.text)
# 	## adding the search results for this planet to my results list
# 	dpla_all_data.append(dpla_data)

# 	## writing out the data for each planet it it's own JSON file for easier searching
# 	json.dump(dpla_data, open(planet+'.json', 'w'), indent=4)

# 	with open (planet+'.csv', 'w') as planet_data:
# 		writer = csv.writer(planet_data)



# json.dump(dpla_all_data, open('dpla_data.json', 'w'), indent=4)


