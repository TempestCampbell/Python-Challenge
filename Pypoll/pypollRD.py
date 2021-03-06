import os
import csv

#Path to collect data from the Resources file
election_csv = os.path.join('Resources', 'election_data.csv')

#Variables
total_votes_cast = 0
candidates={}
candidate_votes={}
candidate_percentage={}
total_votes_won = 0
winner_popularvote = 0

#Read the csv file
with open(election_csv, 'r') as csvfile:
    #Split the data
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)

##The total number of votes cast
    #Read each row of data after the header
    for row in csvreader:
        total_votes_cast += 1
        i = (row[2])

##A complete list of candidates who received votes
###The percentage of votes each candidate won
###The total number of votes each candidate won

#Conditionals to count 
        if i in candidate_votes:
            candidate_votes[i] += 1
        else:
            candidate_votes[i] = 1

    print("Election Results")
    print("-------------------------------")
    print(f'Total Votes:{total_votes_cast}')
    print("-------------------------------")
    
##In addition, your final script should both print the analysis to the terminal and export a text file with the results.

Analysis_file="election_data_results.txt"
csvpath=os.path.join("Analysis", Analysis_file)

with open(csvpath,'w') as text:
    text.write('Election Results')
    text.write('\n -------------------------------')
    text.write(f' \n Total Votes: {total_votes_cast}')

    #For loop to calculate percentage
    for key, votes in candidate_votes.items():
        percentage_votes = round(((votes/total_votes_cast)*100),3)
        print(f'{key}:{percentage_votes}% ({votes})')
        print("-------------------------------")
        text.write(" \n --------------------------------")
        text.write(f'\n {key}:{percentage_votes}% ({votes})')
        
##The winner of the election based on popular vote.
#Conditional to find winner
        if votes > winner_popularvote:
            winner_popularvote = votes
            total_votes_won = key

    print(f"Winner: {total_votes_won}")
    print("--------------------------------")
    text.write("\n --------------------------------")
    text.write(f"\n Winner: {total_votes_won}")
    text.write("\n --------------------------------")
    

