#Program PyBank: an analysis of the financial records of my company, written in Python 3.11.
#
#Read the financial dataset
#
import pandas as pd
financial_data = pd.read_csv ('C:/Users/edwar/Downloads/python-challenge/PyBank/Resources/budget_data.csv')
#
dates = financial_data ['Date']
profitlosses = financial_data ['Profit/Losses']
#
number_of_rows = len (financial_data)
#
total_profitlosses = profitlosses.sum ()
#
total_change = 0
greatest_increase = 0
greatest_decrease = 0
#
#Iterate through all the rows and compute the changes in profit/losses
#
for row_number in range (1, number_of_rows):
#
    change = profitlosses [row_number] - profitlosses [row_number - 1]
#
#Tot up all the changes   
#
    total_change = total_change + change
#
#Compute the greatest increase and decrease and the dates on which they occurred
#
    if change > greatest_increase:
        greatest_increase = change
        date_of_greatest_increase = dates [row_number]
#
    if change < greatest_decrease:
        greatest_decrease = change
        date_of_greatest_decrease = dates [row_number]
#
#Compute the average change
#
average_change = total_change / [number_of_rows - 1]
#
#This block prints my findings to the screen and also writes them to a text file
#
f = open ('C:/Users/edwar/Downloads/python-challenge/PyBank/analysis/PyBank_output_file.txt', 'a')
print ('Financial Analysis')
f.write ('Financial Analysis\n')
print ('----------------------------')
f.write ('----------------------------\n')
print ('Total Months: ', number_of_rows)
f.write ('Total Months: ' + str (number_of_rows) + '\n')
print ('Total: $', total_profitlosses)
f.write ('Total: $' + str (total_profitlosses) + '\n')
print ('Average Change: $', average_change)
f.write ('Average Change: $' + str (average_change) + '\n')
print ('Greatest Increase in Profits: ', date_of_greatest_increase, ' ($', greatest_increase, ')')
f.write ('Greatest Increase in Profits: ' + str (date_of_greatest_increase) + ' ($' + str (greatest_increase) + ')\n')
print ('Greatest Decrease in Profits: ', date_of_greatest_decrease, ' ($', greatest_decrease, ')')
f.write ('Greatest Decrease in Profits: ' + str  (date_of_greatest_decrease) + ' ($' + str (greatest_decrease) + ')')        
f.close