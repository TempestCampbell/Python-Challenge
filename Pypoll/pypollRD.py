import os
import csv

#Path to collect data from the Resources file
election_csv = os.path.join('..', 'Resources', 'election_data.csv')

#Variables
voter_ID =
voter_county = 
candidate_name =

#Read the csv file
with open(election_csv, 'r') as csvfile:
    #Split the data on dash
    csvreader=csv.reader(csvfile, delimiter = ',')

    print(csvreader)

    #Read each row of data after the header
    for row in csvreader:
        print(row)


##The total number of votes cast
total_votes_cast = 

##A complete list of candidates who received votes
list_candidates=

##The percentage of votes each candidate won
percentage_votes = 

##The total number of votes each candidate won
total_votes_won = 

##The winner of the election based on popular vote.
winner_popularvote = 


##In addition, your final script should both print the analysis to the terminal and export a text file with the results.