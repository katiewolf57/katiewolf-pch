# Katie Wolf - PCH final project

# Description
This project uses APIs to collect image records from cultural heritage and science institutions. I used DPLA’s API (https://pro.dp.la/developers/api-codex) and NASA’s Image and Video Library API (https://api.nasa.gov/api.html#Images). I've gathered content related to the plants of our solar system (including Pluto), sorted the results by planet, and pulled out relevant information about the image, including but not limited to institution that houses the image, collection or object ID, other identifying information, rights information, and then descriptive metadata. 
After this information has been compiled, I created a small HTML site that allows the user to see what images are available for each planet in the solar system. This site can be seen in this repository: https://github.com/katiewolf57/katiewolf57.github.io


# How to Use

To run this yourself you'll need an API key from DPLA. You don't need one for NASA's API. 

Start by adding in your API key to DPLA_NASA_scrape.py where noted. 
Save and run the program!

When it's finished running, you'll see a folder labled "planets" at the same level where you've saved these scripts. In this folder, you'll find a folder for each planet (including pluto). Right now, these folders contain JSON files, one for the results from DPLA, another for the results from NASA. 

Now, you run the script JSONtoCSV.py. This script will create a single CSV file for each planet containing each item's title, object record URL, image ID, and image URL. This script will also download all of the images if you'd like it to and put them in a folder labled "images" inside of the appropriate planet folder. Be warned, NASA has roughly 30,000 images for Earth!  

Finally, if you'd like to see some stats on how many images appear for each planet, you can run the graph_info.py script. This will read the JSON files and make pie and bar graphs for both DPLA and NASA. 


You'll also find all of my HTML pages in the HTML folder if you'd like to see how I built that. 
