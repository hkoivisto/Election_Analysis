#  The data we need to retrieve
#1. TOtal number of votes cast
#2. List of candidates who received votes
#3. Number of votes for each candidate
#4. percentage of votes each candidate won
#5. Winner of the election based on popular vote

# import dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable for the file to save
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:

    #Perform Analysis
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    # Write three counties to the file.
    #txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")