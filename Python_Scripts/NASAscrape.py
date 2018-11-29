import re
import requests
import json
import csv
import os
import math

# nasa_all_data = []
# mercury_data = []
# venus_data = []
# earth_data = []
# mars_data = []
# jupiter_data = []
# saturn_data = []
# uranus_data = []
# neptune_data = []
# pluto_data = []

# ## mercury ##
# page_numb=1
# while page_numb < 4:
#     payload = {'q': 'planet AND mercury', 'media_type': 'image', 'page': page_numb}
#     r = requests.get('https://images-api.nasa.gov/search', params=payload)

#     nasa_data = json.loads(r.text)
#     ## adding search results for this planet to results list
#     nasa_all_data.append(nasa_data)
#     mercury_data.append(nasa_data)


#     page_numb = page_numb + 1

# json.dump(mercury_data, open('mercury.json', 'w'), indent=4)

# ## venus ##
# page_numb=1
# while page_numb < 3:
#     payload = {'q': 'planet AND venus', 'media_type': 'image', 'page': page_numb}
#     r = requests.get('https://images-api.nasa.gov/search', params=payload)

#     nasa_data = json.loads(r.text)
#     ## adding search results for this planet to results list
#     nasa_all_data.append(nasa_data)
#     venus_data.append(nasa_data)

#     page_numb = page_numb + 1

# json.dump(venus_data, open('venus.json', 'w'), indent=4)

# ## earth ##

# page_numb=1
# while page_numb < 23:
#     payload = {'q': 'planet AND earth', 'media_type': 'image', 'page': page_numb}
#     r = requests.get('https://images-api.nasa.gov/search', params=payload)

#     nasa_data = json.loads(r.text)
#     ## adding search results for this planet to results list
#     nasa_all_data.append(nasa_data)
#     earth_data.append(nasa_data)

#     page_numb = page_numb + 1

# json.dump(earth_data, open('earth.json', 'w'), indent=4)

# ## mars ##

# page_numb=1
# while page_numb < 19:
#     payload = {'q': 'planet AND mars', 'media_type': 'image', 'page': page_numb}
#     r = requests.get('https://images-api.nasa.gov/search', params=payload)

#     nasa_data = json.loads(r.text)
#     ## adding search results for this planet to results list
#     nasa_all_data.append(nasa_data)
#     mars_data.append(nasa_data)

#     page_numb = page_numb + 1

# json.dump(mars_data, open('mars.json', 'w'), indent=4)


# ## jupiter ##

# page_numb=1
# while page_numb < 7:
#     payload = {'q': 'planet AND jupiter', 'media_type': 'image', 'page': page_numb}
#     r = requests.get('https://images-api.nasa.gov/search', params=payload)

#     nasa_data = json.loads(r.text)
#     ## adding search results for this planet to results list
#     nasa_all_data.append(nasa_data)
#     jupiter_data.append(nasa_data)

#     page_numb = page_numb + 1

# json.dump(jupiter_data, open('jupiter.json', 'w'), indent=4)


# ## saturn ##

# page_numb=1
# while page_numb < 6:
#     payload = {'q': 'planet AND saturn', 'media_type': 'image', 'page': page_numb}
#     r = requests.get('https://images-api.nasa.gov/search', params=payload)

#     nasa_data = json.loads(r.text)
#     ## adding search results for this planet to results list
#     nasa_all_data.append(nasa_data)
#     saturn_data.append(nasa_data)

#     page_numb = page_numb + 1

# json.dump(saturn_data, open('saturn.json', 'w'), indent=4)

# ## uranus ##

# page_numb=1
# while page_numb < 3:
#     payload = {'q': 'planet AND uranus', 'media_type': 'image', 'page': page_numb}
#     r = requests.get('https://images-api.nasa.gov/search', params=payload)

#     nasa_data = json.loads(r.text)
#     ## adding search results for this planet to results list
#     nasa_all_data.append(nasa_data)
#     uranus_data.append(nasa_data)

#     page_numb = page_numb + 1

# json.dump(uranus_data, open('uranus.json', 'w'), indent=4)

# ## neptune ##

# page_numb=1
# while page_numb < 3:
#     payload = {'q': 'planet AND neptune', 'media_type': 'image', 'page': page_numb}
#     r = requests.get('https://images-api.nasa.gov/search', params=payload)

#     nasa_data = json.loads(r.text)
#     ## adding search results for this planet to results list
#     nasa_all_data.append(nasa_data)
#     neptune_data.append(nasa_data)

#     page_numb = page_numb + 1

# json.dump(neptune_data, open('neptune.json', 'w'), indent=4)

# ## pluto ##

# page_numb=1
# while page_numb < 5:
#     payload = {'q': 'planet AND pluto', 'media_type': 'image', 'page': page_numb}
#     r = requests.get('https://images-api.nasa.gov/search', params=payload)

#     nasa_data = json.loads(r.text)
#     ## adding search results for this planet to results list
#     nasa_all_data.append(nasa_data)
#     pluto_data.append(nasa_data)

#     page_numb = page_numb + 1

# json.dump(pluto_data, open('pluto.json', 'w'), indent=4)

# json.dump(nasa_all_data, open('nasadata.json', 'w'), indent = 4)


# ## organizing the JSON files

# planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']

# for planet in planets:
#     os.rename(planet + '.json', './' + planet + '/' + planet + '_nasa' + '.json')




nasa_all_data = []


planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']

## looping thorugh each planet ##
for planet in planets:

    ## start at page one ## 
    

    ## where the data will go ##
    planet_data = []


    print('Looking at ' + planet + '!\n')

    payload = {'q':planet, 'media_type': 'image', 'page': page}
    r = requests.get('https://images-api.nasa.gov/search', params=payload)

    nasa_data = json.loads(r.text)

    ## adding up how many pages are needed: total hits, rounded up, and then divided by 100 (total items per page)
    total_hits = nasa_data['collection']['metadata']['total_hits']
    total_pages = math.ceil(total_hits / 100)

    page = 1

    while page <= total_pages:
        

        payload = {'q': planet, 'media_type': 'image', 'page': page}
        r = requests.get('https://images-api.nasa.gov/search', params=payload)

        nasa_data = json.loads(r.text)

        # add  in the data
        planet_data.append(nasa_data)



    json.dump(planet_data, open(planet + '.json', 'w'), indent=4)

