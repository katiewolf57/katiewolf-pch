import re
import requests
import json
import csv
import os

planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']


dpla_base = 'https://dp.la/thumb/'
nasa_base = 'https://images-assets.nasa.gov/image/'

print("\nMaking CSV files with the item's title and URL")

titles = []
object_records = []
image_ids = []
image_urls = []

## writing DPLA data to csv ##
for planet in planets:
    dpla = open('./planets/' + planet + '/' + planet + '_dpla.json', 'r')
    dpla_data = json.load(dpla)
    dpla_data = dpla_data['docs']

    print('Writing ' + planet + ' csv for DPLA JSON file!')
    ## pulling title info
    for item in dpla_data:
        title = item['sourceResource']['title']
        titles.append(title)

    ## pulling object record url
    for item in dpla_data:
        object_record = item['isShownAt']
        object_records.append(object_record)

    ## pulling image id
    for item in dpla_data:
        image_id = item['id']
        image_ids.append(image_id)


    # pulling image url
    for item in dpla_data:
        image_url = item['object']
        image_urls.append(image_url)

	## writing to csv ##
    with open('./planets/' + planet + '/' + planet + '.csv', 'w') as results:
        writer = csv.writer(results)
        writer.writerows(zip(titles, object_records, image_ids, image_urls))

	## downloading images ##
    # for i in image_ids:
    #     if not os.path.isfile('./' + planet + '/' + i + '.jpg'):
    #         r = requests.get(dpla_base + str(i))
    #         if r.status_code == 200:
    #             print('Downloading: ', i)
    #             with open('./' + planet + '/' + i +'.jpg', 'wb') as f:
    #                 f.write(r.content)
    #         else:
    #             with open('error_log.txt', 'a') as f:
    #                 f.write("ERROR: ", i + '\n')
    #     else:
    #         print('Already Downloaded: ', i)

	## clearing lists! ##
    del titles[:]
    del object_records[:]
    del image_ids[:]
    del image_urls[:]

results.close()


## writing NASA data to csv ##
for planet in planets:
    nasa = open('./planets/' + planet + '/' + planet + '_nasa.json', 'r')
    nasa_data = json.load(nasa)


    print('Appending ' + planet + ' csv with NASA JSON info!')
	## getting the title info ##
    for section in nasa_data:
        collection = section['collection']
        for item in collection['items']:
            data = item['data']
            for info in data:
                title = info['title']
                titles.append(title)

	## getting the object record url ##
    for section in nasa_data:
        collection = section['collection']
        for item in collection['items']:
            data = item['data']
            for info in data:
                nasa_id = info['nasa_id']
                object_record = 'http://images.nasa.gov/details-' + nasa_id + '.html'
                object_records.append(object_record)

	## getting the image id ##
    for section in nasa_data:
        collection = section['collection']
        for item in collection['items']:
            data = item['data']
            for info in data:
                image_id = info['nasa_id']
                image_ids.append(image_id)

	## getting the image url ##
    for section in nasa_data:
        collection = section['collection']
        for item in collection['items']:
            links = item['links']
            for info in links:
                image_url = info['href']
                image_urls.append(image_url)

	## appending the csv ##
    with open('./planets/' + planet + '/' + planet + '.csv', 'a') as results:
        writer = csv.writer(results)
        writer.writerows(zip(titles, object_records, image_ids, image_urls))

	## downloading the images ##
    # for i in image_ids:
    #     if not os.path.isfile('./' + planet + '/' + i + '.jpg'):
    #         r = requests.get(nasa_base + str(i) + '/' + i + '~thumb.jpg')
    #         if r.status_code == 200:
    #             print('Downloading: ', i)
    #             with open('./' + planet + '/' + i +'.jpg', 'wb') as f:
    #                 f.write(r.content)
    #         else:
    #             with open('error_log.txt', 'a') as f:
    #                 f.write("ERROR: ", i + '\n')
    #     else:
    #         print('Already Downloaded: ', i)

    del titles[:]
    del object_records[:]
    del image_ids[:]
    del image_urls[:]

results.close()
