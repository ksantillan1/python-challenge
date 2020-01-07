import os
import csv

Data_csv = os.path.join("Resources", "election_data.csv")


with open(Data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)
    
    Data = [row for row in csvreader]
    
    TotalVote = sum(1 for row in Data)
    
    
    CandidateList = []
    for row in Data:
        Candidate = row[2]
        if Candidate not in CandidateList:
            CandidateList.append(Candidate)
            
    Candidate1 = 0
    Candidate2 = 0
    Candidate3 = 0
    Candidate4 = 0
    
    for row in Data:
        Candidate = row[2]
        if Candidate == CandidateList[0]:
            Candidate1 = Candidate1 +1
        if Candidate == CandidateList[1]:
            Candidate2 = Candidate2 +1
        if Candidate == CandidateList[2]: 
            Candidate3 = Candidate3 +1
        if Candidate == CandidateList[3]:
            Candidate4 = Candidate4 +1
    
    VotesList = [Candidate1,Candidate2,Candidate3,Candidate4]
    MaxVotes = VotesList.index(max(VotesList))
    
    Winner = CandidateList[MaxVotes]
    
    Porcentage1= '{0:.3f}'.format(Candidate1/TotalVote*100)
    Porcentage2= '{0:.3f}'.format(Candidate2/TotalVote*100)
    Porcentage3= '{0:.3f}'.format(Candidate3/TotalVote*100)
    Porcentage4= '{0:.3f}'.format(Candidate4/TotalVote*100)
    
    #Porcentages = [Porcentage1,Porcentage2,Porcentage3,Porcentage4]
    
    #print(Porcentages)
    #print(VotesList)
    #print(CandidateList)
    
    print()
    print("Election Results")
    print("---------------------------------------")
    print("Total Votes:  "+ str(TotalVote))
    print("---------------------------------------")
    print(CandidateList[0] + ": " + str(Porcentage1) + "% (" + str(Candidate1)+")") 
    print(CandidateList[1] + ": " + str(Porcentage2) + "% (" + str(Candidate2)+")") 
    print(CandidateList[2] + ": " + str(Porcentage3) + "% (" + str(Candidate3)+")") 
    print(CandidateList[3] + ": " + str(Porcentage4) + "% (" + str(Candidate4)+")") 
    print("---------------------------------------")
    print("Winner: " + Winner)
    print("---------------------------------------")
    
    
    
    
    