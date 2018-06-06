# import libraries
import os
import csv
	
# navigate to file
csvpath = os.path.join('raw_data/employee_data1.csv')
	
# declare variables
empid = []
fname = []
lname = []
dob = []
ssn = []
state = []
	
# state dictionary
state_abbrev = {
	  'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
	  'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
	  'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
	  'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN',
	  'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV',
	  'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC',
	  'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA',
	  'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX',
	  'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV',
	  'Wisconsin': 'WI', 'Wyoming': 'WY',
	}
	
# read csv file
with open(csvpath, newline = '') as csvfile:
	  csvreader = csv.reader(csvfile, delimiter = ',')
	  next(csvreader, None)
	
    # loop through file
	  for row in csvreader:
	      empid.append(row[0])
	
        # creating 2 lists from 'name' column
	      name = row[1].split(" ") 
	      fname.append(name[0])
	      lname.append(name[1]) 
	
        # change birthday format
	      bdate = row[2].split("-") 
	      new_db = bdate[1] + "/" + bdate[2] + "/" + bdate[0] 
	      dob.append(new_db)
	
        # change ssn format
	      ssn_split = row[3].split("-") # splitting ssn by '-'
	      new_ssn = "***-**-" +ssn_split[2] # formatting ssn
	      ssn.append(new_ssn) # appending formatted ssn
	
        # state abbreviations
	      state.append(state_abbrev[row[4]])
	
# create a zip
employees = zip(empid, fname, lname, dob, ssn, state)
	
# create new csv file
output_file = os.path.join('employee_data_new1.csv')
	
# write the new file
with open(output_file, 'w', newline = '') as csvfile:
	  writer = csv.writer(csvfile, delimiter = ',')
	
    # rewriting columne headers
	  writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])
	
    # populating the data
	  for employee in employees:
	      writer.writerow(employee)