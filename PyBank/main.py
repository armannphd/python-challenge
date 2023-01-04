# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# csvpath = os.path.join('PyBank/resources/budget_data.csv')
csvpath = os.path.join('resources' , 'budget_data.csv')
# csvpath = os.path.join('PyBank' , 'resources' , 'budget_data.csv')
# csvpath = os.path.join('/Users/a/Desktop/ClassFolder/Module03/Module03_Challenge/python-challenge/PyBank/Resources/budget_data.csv')
# csvpath = os.path.join('..' , 'PyBank', 'resources' , 'budget_data.csv')



# setting up the lists
profit_losses_list = []
diff_btwn_month_list = []
date_list = []

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

# to account for the header within the CSV file

    csv_header = next(csvreader)

    for row in csvreader:
        profit_losses_list.append(int(row[1]))
        
# need to create a Date list in order to return the max and min values later

        date_list.append(row[0])

    net_total = sum(profit_losses_list)
    total_months = (len(profit_losses_list))
 
# subtract 1 as calculation begins with second month subtracted from first month

for x in range(total_months - 1):

# x+1 as taking the second value in  the list and stracting from previous value

    diff_btwn_months = (profit_losses_list[x+1]) - (profit_losses_list[x])

# create a new list with values of differences between consecutive months

    diff_btwn_month_list.append(diff_btwn_months)
    
# sum up all the differences between consecutive months

    change_in_pl = sum(diff_btwn_month_list)

# need to subtract 1 as start with second month subtracted from first month

    avg_change_in_pl = change_in_pl / (total_months - 1)

    max_month_profits_value = max(diff_btwn_month_list)
    min_month_profits_value = min(diff_btwn_month_list)

# index of the max month is against a month list that is off by one, thus add 1

    index_max_month = (diff_btwn_month_list.index(max_month_profits_value)+1)
    index_min_month = (diff_btwn_month_list.index(min_month_profits_value)+1)
    max_month = (date_list[index_max_month])
    min_month = (date_list[index_min_month])
    
# #_______________________________________________________________________________________________________________________________________________________________________________
# Create a function to print all the final results
# Need a for statement before the function is defined

for a in csvpath:
    def final_results(a):

        print("Financial Analysis")
        print('------------------------------------------')

        print("Total Months:" ,total_months)
        print("Total:" ,'${:,.2f}'.format(net_total))
        print("Average Change:",'${:,.2f}'.format(avg_change_in_pl))


        print("Greatest Increase in Profits:",max_month,"(",'${:,.2f}'.format(max_month_profits_value),")")
        print("Greatest Decrease in Profits:",min_month,"(",'${:,.2f}'.format(min_month_profits_value),")")

final_results(a)
# #_______________________________________________________________________________________________________________________________________________________________________________
import sys

output_path = os.path.join('PyBank/analysis/PyBank_Output.txt')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:
    sys.stdout = csvfile 
    final_results(a)