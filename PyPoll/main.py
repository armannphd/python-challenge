import os
import csv

csvpath = os.path.join('PyPoll/Resources/election_data.csv')

# open csv file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    candidates = []
    for row in csvreader:
        candidates.append(row[2])

# establish a set to get unique values, then assign each value in the set a variable
    candidate_names = set(candidates)
    c1, c2, c3 = candidate_names

# establish a function to count the number of times a specific candidate's name appears 
# in the candidate list
    def countif(lst, what_to_count_in_the_lst):
        count = 0
        for value in lst:
            if (value == what_to_count_in_the_lst):
                count += 1
        return count
 
c1_votes = countif(candidates, c1)
c2_votes = countif(candidates, c2)
c3_votes = countif(candidates, c3)

Total_votes = c1_votes + c2_votes + c3_votes

percent_vote_c1 = c1_votes / Total_votes
percent_vote_c2 = c2_votes / Total_votes
percent_vote_c3 = c3_votes / Total_votes

winning_votecount = max(c1_votes, c2_votes, c3_votes)

if winning_votecount == c1_votes:
    winner = c1
elif winning_votecount == c2_votes:
    winner = c2
else:
    winner = c3
# #_______________________________________________________________________________

for a in csvpath:
    def final_results(a):
        
        print('Election Results')
        print('--------------------------------------------')

        # note the formatting to get the comma separator for numbers

        print("Total Votes:" , "{:,}".format(Total_votes))
        print('--------------------------------------------')

        # note the formatting to get the percentage formatting to 3 decimals


        print(c1, ":" , "{:.3%}".format(percent_vote_c1), "(" , "{:,}".format(c1_votes), ")")
        print()
        print(c2, ":" , "{:.3%}".format(percent_vote_c2), "(" , "{:,}".format(c2_votes), ")")
        print()
        print(c3, ":" , "{:.3%}".format(percent_vote_c3), "(" , "{:,}".format(c3_votes), ")")
        print('--------------------------------------------')
        print('Winner:', winner)

final_results(a)
# # #_______________________________________________________________________________

# Code to write a separate text file of the results
import sys
original_stdout = sys.stdout

with open('PyPoll/analysis/PyPoll_Output.txt', 'w') as f:
    sys.stdout = f 
    final_results(a)

    