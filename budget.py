# read csv
import os
import csv
budget_csv = os.path.join("..", "Resources", "budget_data.csv")

total_months = []
total_profit = []
Average_change = []
Monthly_profit = []

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
#skips column name 
    skip_header = next(csv_reader)
    
    #end here
    
    #Iterates through rows
    for row in csv_reader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))
   
    #end here

    
    #Iterates through total profits
    for i in range(len(total_profit)-1):
        #Difference between months and appends montly prfot change
        Average_change.append(total_profit[i+1]-total_profit[i]) 
        
    #end here
    
    #Calculates the min and max
    Month_max = max(Average_change)
    Month_min = min(Average_change)
    
    #Assigning max and min to appropriate month, adding 1 to asscoiate with changing months
    max_formonth = Average_change.index(max(Average_change))+1#
    min_formonth = Average_change.index(min(Average_change))+1




print(f"total months:{len(total_months)}")
print(f"total profit:{sum(total_profit)}")
print(f"Average Change:{round(sum(Average_change)/len(Average_change),2)}")
print(f"Greatest Increase in profits:{total_months[ max_formonth]},(${Month_max})")
print(f"Greatest Increase in profits:{total_months[ min_formonth]},(${Month_min})")


#end code

#resources: 
    #https://www.w3schools.com/python/ref_list_index.asp
    #https://blog.finxter.com/python-indexerror-list-index-out-of-range/#:~:text=The%20error%20%E2%80%9Clist%20index%20out,index%20is%20out%20of%20range.
    #https://careerkarma.com/blog/python-typeerror-list-object-cannot-be-interpreted-as-an-integer/
    #https://evanhahn.com/python-skip-header-csv-reader/



