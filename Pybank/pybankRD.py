import os
import csv

#Path to collect data from the Resources file
budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

#Variables
buget_date=
budget_month=
budget_year=



#Read the csv file
with open(budget_csv, 'r') as csvfile:
    #Split the data on dash
    csvreader=csv.reader(csvfile, delimiter = '-')

    print(csvreader)

    #Read each row of data after the header
    for row in csvreader:
        print(row)


##The total number of months included in the dataset
total_months=

##The net total amount of "Profit/Losses" over the entire period
net_total=

##The average of the changes in "Profit/Losses" over the entire period
average_change=

##The greatest increase in profits (date and amount) over the entire period
greaster_increase_profit=

##The greatest decrease in losses (date and amount) over the entire period
greatest_decrease_loss=

##In addition, your final script should both print the analysis to the terminal and export a text file with the results.

