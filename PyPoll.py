# Create file paths across operating systems
import os
# module for reading csv files
import csv

# pass/join individual sub components 
csvpath = os.path.join('Resources','election_data.csv')

Create Function ('poll_results')

# Define variables
total_votes_cast = 0
voters_candidates = []
votes_for_candidate = []
% = 0

#Start loop through rows
for row in data:
    #Begin count for number of votes
     total_votes-cast += 1   
    #append candidates list
     voters_candidates.append(row[2])
    #create list of votes
    votes_for_candidate.append(row[2])

# Open and read csv
with open(election_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)

    #print(f"Header: {csv_header}")
    # This prints -->> Header: Voter ID,Country,Candidate
    # Read through each row of data after the header
   

    # Sort the list by default ascending order
    sorted_list = sorted(voters_candidates)

    #sorted_list = sorted(voters_candidates, reverse=True) 
    #sorted_list.sort(reverse=True) 

    #for key, group in groupby(sorted_list):
    
    # Arrange the sorted list by most common outcomes
    arrange_list = sorted_list

    #count votes per candidate in most common outcome order and append to a list
    count_candidate = Counter (arrange_list) 
    votes_for_candidate.append(count_candidate.most_common())

    # calculate the percentage of votes per candicate in 3 digital points
    for item in votes_for_candidate:
       
        first_rank = format((item[0][1])*100/(sum(count_candidate.values())),'.3f')
        second_rank = format((item[1][1])*100/(sum(count_candidate.values())),'.3f')
        third_rank = format((item[2][1])*100/(sum(count_candidate.values())),'.3f')
        fourth_rank = format((item[3][1])*100/(sum(count_candidate.values())),'.3f')
          
    #print(c.most_common())
    #print(c.values())
    #print(c.keys())
    #print(sum(c.values()))
    
# -->>  Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {sum(count_candidate.values())}")
print("-------------------------")
print(f"{votes_for_candidate[0][0][0]}: {first_rank}% ({votes_for_candidate[0][0][1]})")
print(f"{votes_for_candidate[0][1][0]}: {second_rank}% ({votes_for_candidate[0][1][1]})")
print(f"{votes_for_candidate[0][2][0]}: {third_rank}% ({votes_for_candidate[0][2][1]})")
print(f"{votes_for_candidate[0][3][0]}: {fourth_rank}% ({votes_for_candidate[0][3][1]})")
print("-------------------------")
print(f"Winner:  {votes_for_candidate[0][0][0]}")
print("-------------------------")
