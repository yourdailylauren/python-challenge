import csv
import os

#name the path to the CSV file
csv_file_path = '/Users/laurenpescarus_razeware/Desktop/MSU Course/Classwork/python-challenge/python-challenge/PyPoll/Resources/election_data.csv'

#outline variables to store election analysis data
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

#open and read the CSV file
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)

    #skip the header row
    header = next(csv_reader)

    for row in csv_reader:
        #find the candidate information from the current row
        voter_id = row[0]
        candidate_name = row[2]

        #count the total number of votes
        total_votes += 1

        #track candidate votes and percentages
        if candidate_name in candidates:
            candidates[candidate_name]["votes"] += 1
        else:
            candidates[candidate_name] = {"votes": 1}

#find the winner based on the popular vote
for candidate, data in candidates.items():
    candidate_votes = data["votes"]
    candidate_percentage = (candidate_votes / total_votes) * 100
    candidates[candidate]["percentage"] = candidate_percentage

    if candidate_votes > winner_votes:
        winner = candidate
        winner_votes = candidate_votes

#create the output file path
output_folder = '/Users/laurenpescarus_razeware/Desktop/MSU Course/Classwork/python-challenge/python-challenge/PyPoll/Analysis'
os.makedirs(output_folder, exist_ok=True)
output_file_path = os.path.join(output_folder, 'output.txt')

#print the election results text
output_text = f"Election Results" \
              f"-------------------------" \
              f"Total Votes: {total_votes}" \
              f"-------------------------"

for candidate, data in candidates.items():
    candidate_votes = data["votes"]
    candidate_percentage = data["percentage"]
    output_text += f"{candidate}: {candidate_percentage:.3f}% ({candidate_votes})"

output_text += f"-------------------------" \
               f"Winner: {winner}" \
               f"-------------------------"

#write the output to a text file
with open(output_file_path, 'w') as output_file:
    output_file.write(output_text)

#display the results in the terminal
print(output_text)
