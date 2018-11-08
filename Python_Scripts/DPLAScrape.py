import re
import requests
import json
import csv


## putting in my API key
keykey = json.load(open('/Users/kwolf10/Desktop/PCH/GitHub/katiewolf-pch/JSON_files/api.json', 'r'))
dpla_token = keykey['DPLA_token']

print (dpla_token)

## making an empty list so I can fill it with all my search results
dpla_all_data = []
## all the planets I will be searching over (including pluto b/c it can still look nice)
planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']


# looping through my planet list
# page size is 500 and there are NOT more than 500 results for each planet --> don't have to loop through multiple pages

for planet in planets:
	print("Looking at " + planet + '!\n')
	payload = {'q': 'planet+AND+' + planet, 'page_size':500, 'api_key': dpla_token}
	r = requests.get('https://api.dp.la/v2/items', params = payload)

	dpla_data = json.loads(r.text)
	## adding the search results for this planet to my results list
	dpla_all_data.append(dpla_data)

	## writing out the data for each planet it it's own JSON file for easier searching
	json.dump(dpla_data, open(planet+'.json', 'w'), indent=4)



	print("Made a " + planet + " JSON file\n")



json.dump(dpla_all_data, open('dpla_data.json', 'w'), indent=4)


## now writing out the info to csv files ##

print("\nNow we're making CSV files with the item's title and URL! \n")

object_urls = []
titles = []

for planet in planets:

	f = open(planet + '.json', 'r')
	planet_data = json.load(f)
	planet_data = planet_data['docs']


	for item in planet_data:
		l_url = item['isShownAt']
		object_urls.append(l_url)
	

	for item in planet_data:
		l_title = item['sourceResource']['title']
		titles.append(l_title)


	with open(planet + '.csv', 'w') as results:
		wr = csv.writer(results)
		wr.writerows(zip(object_urls, titles))


	title_count = str(len(titles))
	url_count = str(len(object_urls))

	print("\nThere should be " + title_count + " titles and " + url_count + " urls")

	if title_count != url_count:
		print("WATCH OUT! Those numbers are different!\n")
	else:
		print("Those numbers match! All good!\n")

	del object_urls[:]
	del titles[:]