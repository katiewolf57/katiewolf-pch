import json
import csv
import os
import matplotlib.pyplot as plt
import numpy as np

planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
fields = ['planet', 'dpla', 'nasa']
dpla_counts = []
nasa_counts = []
total_counts =[]

for planet in planets:
    print('Counting hits for ' + planet + '!')
    dpla = open('./planets/' + planet + '/' + planet + '_dpla.json', 'r')
    dpla_data = json.load(dpla)

    dpla_count = dpla_data['count']
    dpla_counts.append(dpla_count)

    print('DPLA had ' + str(dpla_count) + ' hits for ' + planet + '!')

    nasa = open('./planets/' + planet + '/' + planet + '_nasa.json', 'r')
    nasa_data = json.load(nasa)

    nasa_count = nasa_data[1]['collection']['metadata']['total_hits']
    nasa_counts.append(nasa_count)

    print('NASA had ' + str(nasa_count) + ' hits for ' + planet + '!')

    total_count = (nasa_count + dpla_count)
    total_counts.append(total_count)
    print('There were a total of ' + str(total_count) + ' hits for this planet!')

with open('./planets/planet_counts.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
    writer.writerows(zip(planets, dpla_counts, nasa_counts))

print('Made a CSV file for you!')

## making DPLA charts ##
print('Making charts of DPLA images for you!')

## donut chart ##
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']

data = dpla_counts

plt.pie(data)

circle = plt.Circle((0,0), 0.6, color='white')
p = plt.gcf()
p.gca().add_artist(circle)

ax.legend(planets, title='Planets', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

ax.set_title("Planet Images in DPLA")

plt.show()

## bar graph ##
n_groups = 9

fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, dpla_counts, bar_width,
                 alpha=opacity,
                 color='b',
                 label='DPLA')

plt.xlabel('Planet')
plt.ylabel('Number of Images')
plt.title('Planet Images')
plt.xticks(index, ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto'))
plt.legend()

plt.tight_layout()
plt.show()

## NASA charts ##
print('Making a chart of NASA images for you!')

## pie chart ##
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']

data = nasa_counts

plt.pie(data)

circle = plt.Circle((0,0), 0.6, color='white')
p = plt.gcf()
p.gca().add_artist(circle)

ax.legend(planets, title='Planets', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

ax.set_title("Planet Images in NASA's Image Library")

plt.show()

## bar graph ##
n_groups = 9
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, nasa_counts, bar_width,
                 alpha=opacity,
                 color='b',
                 label='NASA')

plt.xlabel('Planet')
plt.ylabel('Number of Images')
plt.title('Planet Images')
plt.xticks(index, ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto'))
plt.legend()

plt.tight_layout()
plt.show()
