# PyPoll

# Import CSV File
import csv

# File Location on Local Drive
location = "C:/Users/richa/OneDrive/Desktop/Data BootCamp/Homework/Python-Challenge/python-challenge/PyPoll/Resources/"
pypollfile = location+"PyPoll_Resources_election_data.csv"

# Arrays to Pull Data from CSV

# Array for number of unique voters
voterid = []

# Array for the order of candidates per voterid
candidate = []

# Array for unique candidate names
candidate_list = []

# Array for total number of votes per candidate
candidate_votes = []

# Array for percentage of votes each candiate received
percent = []

# Open CSV File
with open(pypollfile, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
# Identify the header and store it
    csv_header = next(csvfile)

# Created two arrays, 1 for voterids and 1 for the candidate per voterid
    for row in csvreader:
        voterid.append(row[0])
        candidate.append(row[2])

# Created a unique list of candidates in the polls
    for x in candidate:
        if x not in candidate_list:
            candidate_list.append(x)
            y = len(candidate_list)

# Created an Array to make a table to tally votes and percentages each candidate received
    for counter in range(0, y):
        candidate_votes.insert(1, 0)
        percent.insert(1, 0)

# Tallies votes into candidate specific sections in the array
    while y > 0:
        y = y-1
        for count in range(0, len(candidate)):
            if candidate_list[y-1] == candidate[count]:
                candidate_votes[y-1] += 1

# Calculated the percentages per candidate
    for p in range(0, len(percent)):
        percent[p] = candidate_votes[p]/len(voterid)

# Printing of the voting summary
    print("Election Results")
    print("-------------------------")
    print(f'Total Votes: {len(voterid)}')
    print("-------------------------")
# f string to print all of the candidates tallies and percentages
    for d in range(0, len(candidate_list)):
        print(f'{candidate_list[d]}: {percent[d]:.3%} ({candidate_votes[d]})')
    print("-------------------------")

# Created a function to sift through candidate total votes to announce the winner
    winner = candidate_votes[0]
    winnern = f'Winner: {candidate_list[0]}'
    for pv in range(0, len(candidate_votes)-1):
        if winner < candidate_votes[pv]:
            winner = candidate_votes[pv]
            winnern = f'Winner: {candidate_list[pv]}'
    print(winnern)
    print("-------------------------")
