import os
import csv

# Define the path to the CSV file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Initialize variables
total_months = 0
total_net = 0
net_change_list = []
month_of_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999]

# Read the CSV file
with open(csvpath, 'r') as data:
    csvreader = csv.reader(data, delimiter=',')
    
    # Skip the header row
    csv_header = next(csvreader)
    
    # Read the first row
    first_row = next(csvreader)
    total_months += 1
    total_net += int(first_row[1])
    previous_net = int(first_row[1])

    # Loop through the rest of the rows
    for row in csvreader:
        total_months += 1
        total_net += int(row[1])
        
        # Calculate the net change
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list.append(net_change)
        month_of_change.append(row[0])
        
        # Determine the greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase = [row[0], net_change]
        
        # Determine the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease = [row[0], net_change]

# Calculate the average net change
average_change = sum(net_change_list) / len(net_change_list)

# Print the results
print("Financial Analysis")
print("-------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_net}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Write the results to a text file
with open('results.txt', 'w') as file:
    file.write("Financial Analysis\n")
    file.write("-------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_net}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
