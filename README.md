# Election_analysis

## Project Overview
AColorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the toatal number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the toal number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
 - Data Source: election_results.csv
 - Software: Python 3.7.6, Visual Studio Code, 1.38.1 
 
 ## Election Audit Results
 The analysis of the election show that:
  - There were 369,711 votes cast in the election.
  - The county results were:
    - Jefferson County represented 10.5% of the toal vote with 38,855 votes.
    - Denver County represented 82.8% of the total vote with 306,055 votes.
    - Arapahoe County represented 6.7% of the total vote with 24,801 votes.
  - The county withthe most votes was:
    - Denver County, with 82.8% of the total vote and 306,055 votes.
  - The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
  - The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 votes.
    
  ![Election_summary]
    
  ## Election Audit Summary
  This audit script is designed so that any csv file of election results can be processed. 
  Minor modifications that could be needed for additioanl types of elections include:
   - If the election district differ from 'counties' as seenin this analysis, the hardcoded output verbage can be changed to match whichever type of district is represented.
   - If the election winner is required to reach a threshold percentage of votes, rather than just simple majority, a condition can be added to reflect this.
    - This modification could achieved as such:
    
    ...
    if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    ...
    
   Modified to:
   
    ...
    if (votes > winning_count) and (vote_percentage > winning_percentage) and vote_percentage > 50:
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    else:
            winning_candidate = "No winner determined. No candidate recieved the threshhold percentage."
    ...
   
   
    

  
