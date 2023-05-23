# This code scrapes the data which is required to my new youtube video.

import requests
from bs4 import BeautifulSoup
import csv

# Get the page content and create a soup object
url = "https://en.wikipedia.org/wiki/List_of_space_travellers_by_first_flight"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Find the table containing the data we want to scrape 
table = soup.find('table', class_='wikitable sortable') 
rows = table.findAll('tr') # Get all the rows in the table 
csvFile = open('space-travellers-data.csv', 'wt+', encoding="utf-8", newline='') # Open a csv file for writing 
writer = csv.writer(csvFile) # Create a writer object 
try: 

    for row in rows: # Loop through each row in the table 

        csvRow = [] # Create an empty list that will hold our row data 

        for cell in row.findAll(['td', 'th']): # Loop through each cell in the row  

            csvRow.append(cell.get_text().strip()) # Get the text from each cell and add it to our list  

        writer.writerow(csvRow) # Write the row to our csv file  
finally:  

    csvFile.close()
