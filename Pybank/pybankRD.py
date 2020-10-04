import os
import csv
import statistics

#Path to collect data from the Resources file
budget_csv = os.path.join('Resources', 'budget_data.csv')

#Define the function
#def print_totals(budget_data):

#Variables
#budget_month = str(budget_data[0])
#budget_profit_loss = int(budget_data[1])
total_months= 0
net_total=0
current_month_profit=0
previous_month_profit=867884
profit_change=0
profit_changeS=[]
budget_monthS=[]

#Read the csv file
with open(budget_csv, 'r') as csvfile:
    #Split the data
    csvreader=csv.reader(csvfile, delimiter = ',')
    header=next(csvreader)

    #Read each row of data after the header
    for row in csvreader:
        total_months +=1
        budget_monthS.append(row[0])
        net_total += int(row[1])
        current_month_profit= int(row[1])


##The total number of months included in the data set
        if total_months >1:
            profit_change = current_month_profit - previous_month_profit
            profit_changeS.append(profit_change)
            previous_month_profit=current_month_profit
            
    print(f'Total Months:{total_months}')

##The net total amount of "Profit/Losses" over the entire period
net_total = sum(profit_changeS)

print(f'Net Total Profit/Losses over an Entire Period: ${net_total}')

##The average of the changes in "Profit/Losses" over the entire period
average_change = round(net_total/total_months-1)

print(f'Average Changes in Profit/Losses Over an Entire Period: ${average_change}')

##The greatest increase in profits (date and amount) over the entire period
greastest_increase_profit= max(profit_changeS)
greatest_increase_month=budget_monthS[profit_changeS.index(greastest_increase_profit)]

print(f'Greastest Increase in Profits Over the Entire Period: {greatest_increase_month} (${greastest_increase_profit})')

##The greatest decrease in losses (date and amount) over the entire period
greatest_decrease_loss = min(profit_changeS)
greatest_decrease_month = budget_monthS[profit_changeS.index(greatest_decrease_loss)]

print(f'Greastest Decrease in Profits Over the Entire Period: {greatest_decrease_month} (${greatest_decrease_loss})')

##In addition, your final script should both print the analysis to the terminal and export a text file with the results.

Analysis_file= "buget_data_results.txt"
csvpath=os.path.join("Analysis","Analysis_file")
with open (csvpath,'w') as text:
    text.write("Financial Analysis")
    text.write('\n'+"--------------------------")
    text.write(f'\n Total Months:{total_months}')
    text.write(f'\n Net Total Profit/Losses over an Entire Period: ${net_total}')
    text.write(f'\n Average Changes in Profit/Losses Over an Entire Period: ${average_change}')
    text.write(f'\n Greastest Increase in Profits Over the Entire Period: {greatest_increase_month} (${greastest_increase_profit})')
    text.write(f'\n Greastest Decrease in Profits Over the Entire Period: {greatest_decrease_month} (${greatest_decrease_loss})')
