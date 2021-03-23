# PyBank
#Import OS for File Navigation
import os

# Import CSV File
import csv

# Import Sys to print to .txt
import sys

# Original stdout
orig = sys.stdout

# .txt file
txt = os.path.join("analysis", "PyBank_Summary.txt")

# File Path on Local Drive
pybankfile = os.path.join("Resources", "PyBank_Resources_budget_data.csv")

# Total Months
mtot = []

# Array of Monthly Change in Money
mchange = []

# Total of All Profits/Losses
sumtot = 0.0

# Array of Monthly Changes
dif = []

# Sum of All Monthly Changes
avchange = 0.0

# Greatest Monthly Change
greatest = 0.0

# Lowest Monthly Change
lowest = 0.0


# Read in the CSV file
with open(pybankfile, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# identify and skip header
    csv_header = next(csvfile)

# Append Months and Monthly Profits/Losses to Array
    for row in csvreader:
        mtot.append(row[0])
        mchange.append(row[1])

# Add all values of Monthly Profits/Losses
    for i in range(0, len(mtot)):
        sumtot = sumtot+float(mchange[i])

# Average of all Monthly Changes
        if i < 85:
            dif.append(float(mchange[i+1])-float(mchange[i]))
            avchange = avchange+dif[i]

# Finding the Greatest Increase and Decrease in Profits
            if float(mchange[i+1])-float(mchange[i]) > greatest:
                greatest = float(mchange[i+1])-float(mchange[i])
                yearg = mtot[i+1]
            if float(mchange[i+1])-float(mchange[i]) < lowest:
                lowest = float(mchange[i+1])-float(mchange[i])
                yearl = mtot[i+1]

# Print Summary Report
    print("Financial Analysis")
    print("----------------------------")
    print(f'Total Months: {len(mtot)}')
    print(f'Total: ${int(sumtot)}')
    print(f'Average Change: {round(avchange/len(dif),2)}')
    print(f'Greatest Increase in Profits: {yearg} ({round(greatest)})')
    print(f'Greatest Decrease in Profits: {yearl} ({round(lowest)})')

# export to .txt
    sys.stdout = open(txt, 'wt')
    print("Financial Analysis")
    print("----------------------------")
    print(f'Total Months: {len(mtot)}')
    print(f'Total: ${int(sumtot)}')
    print(f'Average Change: {round(avchange/len(dif),2)}')
    print(f'Greatest Increase in Profits: {yearg} ({round(greatest)})')
    print(f'Greatest Decrease in Profits: {yearl} ({round(lowest)})')
    sys.stdout = orig
