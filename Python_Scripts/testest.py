import csv
import requests
import os.path



base = 'https://dp.la/thumb/'

images = []

with open('/Users/kwolf10/Desktop/PCH/GitHub/katiewolf-pch/CSV_files/jupiter.csv', 'r') as csv_file:
	reader = csv.reader(csv_file)
	for row in reader:
		images.append(row[2])


print(images)

for i in images:
	if not os.path.isfile('./thumbs/'+i+'.jpg'):
		r = requests.get(base + str(i))
		if r.status_code == 200:
			print("Downloading: ", i)
			with open('./thumbs/'+ i + '.jpg', 'wb') as f:
				f.write(r.content)

		else:
			with open('error_log.txt', 'a') as f:
				f.write("ERROR:" + i + '\n')

	else:
		print("DOWNLOADED", i)
