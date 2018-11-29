import re
import requests
import json
import csv
import os

planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']



## downloading DPLA images, adding DPLA information to relevant CSV files ##

# print("\nNow we're making CSV files with the item's title and URL! \n")

# object_urls = []
# titles = []
# images = []

# ## base of the image url for downloading
# base = 'https://dp.la/thumb/'


# for planet in planets:

# 	## opening up the JSON file to search through for relevant info
# 	f = open('./' + planet + '/' + planet + '_dpla.json', 'r')
# 	planet_data = json.load(f)
# 	planet_data = planet_data['docs']

# 	## pulling the collection url for the item
# 	for item in planet_data:
# 		l_url = item['isShownAt']
# 		object_urls.append(l_url)

# 	## pulling the title for the item
# 	for item in planet_data:
# 		l_title = item['sourceResource']['title']
# 		titles.append(l_title)


# 	## pulling the image id for the itme
# 	for item in planet_data:
# 		image = item['id']
# 		images.append(image)

# 	## making a csv with the urls, titles, and image ids
# 	## putting it in the planet folder
# 	with open('./' + planet + '/' + planet + '.csv', 'w') as results:
# 		wr = csv.writer(results)
# 		wr.writerows(zip(object_urls, titles, images))


# 	## writing images to the planet folder
# 	for i in images:

# 	## making sure not to download an image if it's already been downloaded
# 		if not os.path.isfile('./' + planet + '/' +i+'.jpg'):
# 			r = requests.get(base + str(i))
# 			if r.status_code == 200:
# 				print("Downloading: ", i)
# 				with open('./' + planet + '/'+ i + '.jpg', 'wb') as f:
# 					f.write(r.content)

# 	## making sure that if any images aren't found/don't exist any more, it's reported so I can deal with them
# 			else:
# 				with open('error_log.txt', 'a') as f:
# 					f.write("ERROR:" + i + '\n')

# 		else:
# 			print("ALREADY DOWNLOADED", i)


# 	title_count = str(len(titles))
# 	url_count = str(len(object_urls))
# 	image_count = str(len(images))

# 	print("\nThere should be " + title_count + " titles and " + url_count + " urls and  " + image_count + " images for " + planet)

# 	## alerting me if there's a discprepancy between title/url/image count
# 	if title_count > url_count:
# 		print("WATCH OUT! There are more titles than urls!\n")
# 	elif title_count > image_count:
# 		print("WATCH OUT! There are more titles than images!\n")
# 	elif url_count > title_count:
# 		print("WATCH OUT! There are more urls than titles!\n")
# 	elif url_count > image_count:
# 		print("WATCH OUT! There are more urls than images!\n")
# 	elif image_count > title_count:
# 		print("WATCH OUT! There are more images than titles!\n")
# 	elif image_count > url_count:
# 		print("WATCH OUT! There are more images than urls!\n")
# 	else:
# 		print("Those numbers match! All good!\n")

# 	## clearing out the lists so they can be counted for the next planet
# 	del object_urls[:]
# 	del titles[:]
# 	del images[:]


## downloading NASA images and adding info to relevant CSVs ##

for planet in planets:

	## opening up the JSON file to search through for relevant info
	f = open('./' + planet + '/' + planet + '_nasa.json', 'r')
	planet_data = json.load(f)
	planet_data = planet_data['docs']

	## pulling the collection url for the item
	for item in planet_data:
		l_url = item['isShownAt']
		object_urls.append(l_url)

	# ## pulling the title for the item
	# for item in planet_data:
	# 	l_title = item['sourceResource']['title']
	# 	titles.append(l_title)


	# ## pulling the image id for the itme
	# for item in planet_data:
	# 	image = item['id']
	# 	images.append(image)

	# ## making a csv with the urls, titles, and image ids
	# ## putting it in the planet folder
	# with open('./' + planet + '/' + planet + '.csv', 'w') as results:
	# 	wr = csv.writer(results)
	# 	wr.writerows(zip(object_urls, titles, images))


	# ## writing images to the planet folder
	# for i in images:

	# ## making sure not to download an image if it's already been downloaded
	# 	if not os.path.isfile('./' + planet + '/' +i+'.jpg'):
	# 		r = requests.get(base + str(i))
	# 		if r.status_code == 200:
	# 			print("Downloading: ", i)
	# 			with open('./' + planet + '/'+ i + '.jpg', 'wb') as f:
	# 				f.write(r.content)

	# ## making sure that if any images aren't found/don't exist any more, it's reported so I can deal with them
	# 		else:
	# 			with open('error_log.txt', 'a') as f:
	# 				f.write("ERROR:" + i + '\n')

	# 	else:
	# 		print("ALREADY DOWNLOADED", i)


	# title_count = str(len(titles))
	# url_count = str(len(object_urls))
	# image_count = str(len(images))

	# print("\nThere should be " + title_count + " titles and " + url_count + " urls and  " + image_count + " images for " + planet)

	# ## alerting me if there's a discprepancy between title/url/image count
	# if title_count > url_count:
	# 	print("WATCH OUT! There are more titles than urls!\n")
	# elif title_count > image_count:
	# 	print("WATCH OUT! There are more titles than images!\n")
	# elif url_count > title_count:
	# 	print("WATCH OUT! There are more urls than titles!\n")
	# elif url_count > image_count:
	# 	print("WATCH OUT! There are more urls than images!\n")
	# elif image_count > title_count:
	# 	print("WATCH OUT! There are more images than titles!\n")
	# elif image_count > url_count:
	# 	print("WATCH OUT! There are more images than urls!\n")
	# else:
	# 	print("Those numbers match! All good!\n")

	# ## clearing out the lists so they can be counted for the next planet
	# del object_urls[:]
	# del titles[:]
	# del images[:]
