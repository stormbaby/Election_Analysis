# -*- coding: UTF-8 -*-
#PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
from ctypes import cdll
import os

# Add a variable to load a file from a path.
path = os.getcwd()
#print(path)
file_to_load = os.path.join(path,"Desktop/Election_Analysis", "resources", "election_results.csv")

#print(file_to_load)
# Add a variable to save the file to a path.
file_to_save = os.path.join(path,"Desktop/Election_Analysis", "resources","analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
cand_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.

county_list = []
county_votes_dict = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
largest_county_turnout = 0
county_voter_turnout = 0
candidate = {}
candidates = []


# Read the csv and convert it into a list of dictionaries
candidates = []
#candidates[candidate] = {}
#with open(../resources/election_results.csv) as election_data:
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]


        # If the candidate does not match any existing candidate add it to
        # the candidate list
        #print(candidate_name)
        #print(candidate_options)
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            #candidate_votes.update({"name":candidate_name} )

            candidate_votes.update({candidate_name:0})
            
            
         #   candidate_votes.update({"votes":0})


        #    print(candidate_votes[candidate_name])



        # Add a vote to that candidate's count


    
        current_votes = candidate_votes[candidate_name] 

        current_votes = candidate_votes[candidate_name] + 1
        candidate_votes[candidate_name] = current_votes
       # print(candidate_votes[candidate_name])

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
      #  print(county_name)
       # print(county_list)

        if county_name not in county_list:



            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)
       #     print(county_list)

            # 4c: Begin tracking the county's vote count.
            
            county_votes_dict.update({county_name:0})
       #     county_votes_dict.update({'votes':0})

       #     print(county_votes_dict[county_name])




        # 5: Add a vote to that county's vote count.
    #    print(county_name)
        new_vote = county_votes_dict[county_name]
#        print(county_votes_dict["county_name"])
        county_votes_dict[county_name] = new_vote +1 


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    county_v = 0
    for county_v in  range(len(county_list)):   

        # 6b: Retrieve the county vote count.
        votes_per_county = county_votes_dict[county_list[county_v]]

        # 6c: Calculate the percentage of votes for the county.

        percent_votes =  ( votes_per_county / total_votes) * 100
        # results to the terminal.
        
        county_results_txt = (f"{county_list[county_v]}: {percent_votes:.1f}% ({votes_per_county:,})\n")
        county_results_print = (f"{county_list[county_v]}: {percent_votes:.1f}% ({votes_per_county:,})")
        print(county_results_print)
        #txt_file.write(f'{county_list[county_v]}: {round(percent_votes,1)}% ({votes_per_county:,})')
        txt_file.write(county_results_txt)
        #print(f'{county_list[county_v]}: {round(percent_votes,1)}% ({votes_per_county:,})')
    #print(candidate_results)
         # 6e: Save the county votes to a text file.

    #txt_file.write(str(votes_per_county))


         # 6f: Write an if statement to determine the winning county and get its vote count.
        #countxx = len(county_votes_dict)
        if county_v == 0:
      #  if( county_votes_dict[i]) == winning_county:
            county_voter_turnout = county_votes_dict[county_list[county_v]]
            winning_county = county_list[county_v]
        elif (county_votes_dict[county_list[county_v]] > county_voter_turnout):
            county_voter_turnout = county_votes_dict[county_list[county_v]]
            winning_county = county_list[county_v]
    # 7: Print the county with the largest turnout to the terminal.
    largest_county = (f'\n' 
    f"--------------------------------\n"
    f'Largest County Turnout: {winning_county}\n'
    f'--------------------------------\n')

    print(largest_county)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(largest_county)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results_txt = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results_print = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})")
        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results_print)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results_txt)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
