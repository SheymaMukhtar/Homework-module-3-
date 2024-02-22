#Work with file path
import os 

#import csv file 
import csv

#Giving python exactly where the file is 
budgetdatapath = os.path.join ('.', 'resources', 'budget_data.csv')

with open (budgetdatapath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
        #print (row)
        print(row[0])

count_rows=(csvfile)
row_count = 0

 # Understand the amount of rows I have by adding a variable 
row_count = 0
    # Look at each line within the file. 
for line in budgetdatapath:
        # calculate the amount of rows within the CSV file.
        row_count += 1

# Print the total number of rows
print("Total number of rows:", row_count)

 #extract the profit_loss with variable 
profit_loss = int(row[2])

total_profit_losses += profit_loss
print("Net Total Amount of Profit/Losses: $" + str(total_profit_losses))

average_change = sum(changes) / len(changes)

# Print results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total_amount}")
print(f"Average Change: ${average_change:.2f}")

 # Skip the header row
next(csvreader)
    
for idx, row in enumerate(csvreader):
        if idx == max_increase_index:
            max_increase_date = row[0]
            max_increase_amount = max_increase

# Print the results
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase_amount})")


average_change = sum(profit_changes) / len(profit_changes)


greatest_increase = max(profit_changes)
greatest_decrease = min(profit_changes)


greatest_increase_index = profit_changes.index(greatest_increase)
greatest_decrease_index = profit_changes.index(greatest_decrease)

greatest_increase_date = dates[greatest_increase_index]
greatest_decrease_date = dates[greatest_decrease_index]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})"
    
print (f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})”)