import csv

data = []

# opening the CSV file
with open('space-travellers-data.csv', mode ='r') as file:
  # reading the CSV file
  csvFile = csv.reader(file)
  counter = 0
  # a = set();
  # displaying the contents of the CSV file
  for lines in csvFile:
    #print(lines)
    size = len(lines);
    if size == 6:
      _,name, nationality, date, firstFlight,_ = lines
      row = [counter, name, nationality, date, firstFlight]
    elif size == 2:
      name, nationality = lines
      row = [counter, name, nationality, date, firstFlight]
    elif size == 3:
      name, nationality, _ = lines
      row = [counter, name, nationality, date, firstFlight]
    data.append(row)
    # a.add(name)
    counter = counter + 1
  # print(len(a))

# Creating the csv file for writing 
csvFile = open('space-travellers.csv', 'wt+', encoding="utf-8", newline='') 
writer = csv.writer(csvFile) # Create a writer object 
try: 

    for row in data: # Loop through each row in data 

        writer.writerow(row) # Write the row to our csv file  
finally:  

    csvFile.close()