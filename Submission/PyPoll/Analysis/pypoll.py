import csv

#Set path for file
csvpath = "Resources/election_data.csv"

#Set variables
vote_number = 0
candidate_dict = {}

#Open the CSV using UTF-B encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Read header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    #Read each row of data after header
    for row in csvreader:

        #count the number of votes in the dataset
        vote_number +=1

        # add to the dictionary
        row_candidate = row[2]
        if row_candidate in candidate_dict.keys():
            candidate_dict[row_candidate] += 1
        else:
            candidate_dict[row_candidate] = 1

#create output
output = f"""Election Results
-------------------------
Total Votes: {vote_number}
-------------------------\n"""

max_cand = ""
max_votes = 0

for candidate in candidate_dict.keys():
    votes = candidate_dict[candidate]
    percent = (votes / vote_number) * 100

    line = f"{candidate}: {round(percent, 3)}% ({votes})\n"
    output += line

    if votes > max_votes:
        max_cand = candidate
        max_votes = votes

last_line = f"""-------------------------
Winner: {max_cand}
-------------------------"""
output+= last_line

print(output)

with(open("output.txt", 'w')as f):
    f.write(output)




