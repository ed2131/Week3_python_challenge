import os
import csv

# Define the path to the CSV file
csvpath = os.path.join('Resources', 'election_data.csv')

# Initialize variables
total_votes = 0
candidates_votes = {}

# Read the CSV file
with open(csvpath, 'r') as data:
    csvreader = csv.reader(data, delimiter=',')
    
    # Skip the header row
    csv_header = next(csvreader)
    
    # Loop through the rows
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        
        if candidate in candidates_votes:
            candidates_votes[candidate] += 1
        else:
            candidates_votes[candidate] = 1

# Print the results
print("Election Results")
print("-------------------")
print(f"Total Votes: {total_votes}")
print("-------------------")

# Determine the winner
winner = max(candidates_votes, key=candidates_votes.get)

for candidate, votes in candidates_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("-------------------")
print(f"Winner: {winner}")
print("-------------------")

# Write the results to a text file
with open('election_results.txt', 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------\n")
    
    for candidate, votes in candidates_votes.items():
        percentage = (votes / total_votes) * 100
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    
    file.write("-------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------\n")
