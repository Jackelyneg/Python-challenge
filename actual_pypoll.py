#reading file
import os
import csv
election_csv = os.path.join("..", "Resources", "election_data.csv")

#end here

#zero values
voter_id = []
voter_county=[]

#length of entire csv
votes = len(election_csv)
khan =len(election_csv)
Correy = len(election_csv)
Li =len(election_csv)
Otool = len(election_csv)

with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    skip_header = next(csv_reader)


#start loop
    for row in csv_reader:
        #appending and assigning columns
        voter_id.append(int(row[0]))
        voter_county.append(row[1])
        candidate = row[2]
        
        #end here
        
        #Counts the unique Voter ID's
        votes = votes + 1

        #Counts how many times each candidate appears in the list
        if candidate =="Khan":
            khan= khan+1
        elif candidate =="Correy":
            Correy=Correy+1
        elif candidate == "Li":
            Li=Li+1
        elif candidate == "O'Tooley":
            Otool = Otool +1

#Calculate percentage  
khan_percentage = (khan/votes)*100
Correy_percentage = (Correy/votes)*100
Li_percentage = (Li/votes)*100
Otool_percentage = (Otool/votes)*100
        
#list of Candidate percentage votes
candidate_list = [khan_percentage,Correy_percentage,Li_percentage,Otool_percentage]


#List of candidate names
candidate_name = ["Khan","Correy","Li","O'Tooley"]

#zip percentage and names
result = zip(candidate_list,candidate_name)
#max result of votes
new_result = max(result)[1]
result_set = (new_result)





print(f"Election Results")
print(f"total votes:{(votes)}")
print(f"khan votes:{round((khan_percentage),1)}%")
print(f"Correy votes:{round((Correy_percentage),1)}%")
print(f"Li votes:{round((Li_percentage),1)}%")
print(f"Otool votes:{round((Otool_percentage),1)}%")
print(f"Winning Candidate:{(result_set)}")

#Resources:
    #https://stackoverflow.com/questions/35921951/zip-key-value-pairs-in-python/35922154
    # https://stackoverflow.com/questions/4002796/python-find-the-min-max-value-in-a-list-of-tuples
    

