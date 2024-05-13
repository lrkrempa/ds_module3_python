import csv

#Set path for file
csvpath = "Resources/budget_data.csv"

#Set variables
month_number = 0
total_profit = 0

#Find changes in profit/losses
last_profit = 0
changes = []
month_change = []

#Open the CSV using UTF-B encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Read header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    #Read each row of data after header
    for row in csvreader:

        #count the number of months in the dataset
        month_number = month_number + 1

        #find sum of total profit
        total_profit = total_profit + int(row[1])

        #No change in FIRST ROW
        if(month_number==1):
            #FIRST ROW so no change
            last_profit = int(row[1])
        else:
            change = int(row[1]) - last_profit
            changes.append(change)
            month_change.append(row[0])

            #reset last month profit
            last_profit = int(row[1])

    average_change= sum(changes) / len(changes)

    max_change =max(changes)
    max_month_index = changes.index(max_change)
    max_month = month_change[max_month_index]

    min_change = min(changes)
    min_month_index = changes.index(min_change)
    min_month = month_change[min_month_index]

    output = f"""Financial Analysis
----------------------------
Total Months: {month_number}
Total: ${total_profit}
Average Change: ${average_change}
Greatest Increase in Profits: {max_month} (${max_change})
Greatest Decrease in Profits: {min_month} (${min_change})"""
    
    print(output)

    with(open("output_text",'w') as f):
        f.write(output)





