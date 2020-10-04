import os
import csv
import statistics

#Path to collect data from the Resources file
budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

#Define the function
#def print_totals(budget_data):

#Variables
#budget_month = str(budget_data[0])
#budget_profit_loss = int(budget_data[1])
total_months= 0


#Read the csv file
with open(budget_csv, 'r') as csvfile:
    #Split the data
    csvreader=csv.reader(csvfile, delimiter = ',')

    print(csvreader)

    #Read each row of data after the header
    for row in csvreader:
        total_months +=1
        print(row)


##The total number of months included in the dataset
total_months=

##The net total amount of "Profit/Losses" over the entire period
net_total = sum(budget_profit_loss)

##The average of the changes in "Profit/Losses" over the entire period
average_change = statistics.mean(round(budget_profit_loss))

##The greatest increase in profits (date and amount) over the entire period
greaster_increase_profit= 

##The greatest decrease in losses (date and amount) over the entire period
greatest_decrease_loss=

##In addition, your final script should both print the analysis to the terminal and export a text file with the results.

