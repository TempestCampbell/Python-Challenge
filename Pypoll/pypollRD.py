import os
import csv
import statistics

#Path to collect data from the Resources file
election_csv = os.path.join('..', 'Resources', 'election_data.csv')

#Define the function
#def votes(election_data):

#Variables
voter_ID = int(election_data[0])
voter_county = str(election_data[1]
Candidate_name = str(election_data[2])
total_votes_cast=0
total_votes_won=0
winner_popularvote=0

#Read the csv file
with open(election_csv, 'r') as csvfile:
    #Split the data
    csvreader=csv.reader(csvfile, delimiter = ',')

    header=next(csvreader)

    #Read each row of data after the header
    for row in csvreader:
        total_votes_cast +=1

        i=(row[2])


##The total number of votes cast
total_votes_cast = len(voter_ID)

##A complete list of candidates who received votes
#list_candidates=

##The percentage of votes each candidate won
#percentage_votes = 

##The total number of votes each candidate won
#total_votes_won = 

##The winner of the election based on popular vote.
#winner_popularvote = 


##In addition, your final script should both print the analysis to the terminal and export a text file with the results.