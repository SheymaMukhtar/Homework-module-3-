import os
import csv

#Locate the file
electiondata = os.path.join('.', 'resources', 'election_data.csv')

#variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# open and read the file
with open(electiondata) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header row
    csv_header = next(csvreader)

    #go through each row and pull the data
    for row in csvreader:
        #count total votes
        total_votes += 1
        #allow terminal to give the candidate name in row 2.
        candidate_name = row[2]
        
        if candidate_name not in candidates:
            candidates[candidate_name] = 1
        
        else:
            candidates[candidate_name] += 1

#print the total votes
print("Total Votes:", total_votes)
print("-------------------------")

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    # Determine the winner
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

print("-------------------------")

print("Winner:", winner)
print("-------------------------")
