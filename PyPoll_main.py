#Program PyPoll: an analysis of votes for a small, rural town, written in Python 3.11.

#Read the election dataset

import pandas as pd
election_data = pd.read_csv ('C:/Users/edwar/Downloads/python-challenge/PyPoll/Resources/election_data.csv')

ballot_id = election_data ['Ballot ID']
county = election_data ['County']
candidate = election_data ['Candidate']

total_votes = len (election_data)

candidates_list = ['' for i in range (10)]

candidates_list [1]  = 'Charles Casper Stockham'

i = 2

for row_number in range (2, total_votes):

    if candidate [row_number] != candidate [row_number - 1]:

        candidates_list [i] = candidate [row_number]

        i = i + 1

for j in range (2, i):

        for k in range (1, j - 1):
            
             if candidates_list [j] == candidates_list [k]:
           
                  candidates_list [j] = ''

f = open ('C:/Users/edwar/Downloads/python-challenge/PyPoll/analysis/PyPoll_output_file.txt', 'a')

f.write ('Election Results\n')

f.write ('-------------------------\n')

f.write ('Total Votes: ' + str (total_votes) + '\n')

f.write ('-------------------------\n')
     
votes = [0 for j in range (i)]

for row_number in range (1, total_votes):

        for j in range (1, i): 
              
             if candidates_list [j] == candidate [row_number]:
                    
                  votes [j] = votes [j] + 1

percentage_votes = [0 for j in range (i)]

for j in range (1, i):

        if votes [j] == 0:
            
             break
      
        percentage_votes [j] = votes [j] / total_votes * 100
      
        f.write (str (candidates_list [j]) + ': ' + str('{:.3f}'.format (percentage_votes [j])) + '% (' + str (votes [j]) + ')\n')

f.write ('-------------------------\n')

winners_vote = 0

for j in range (2, i):

        if votes [j] == 0:
              
              break
      
        elif votes [j] > winners_vote:
             
              winners_vote = votes [j]

              winner = candidates_list [j]

f.write ('Winner: ' + winner + '\n')

f.write ('-------------------------')