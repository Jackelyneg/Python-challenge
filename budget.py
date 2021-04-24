import os
import csv
budget_csv = os.path.join("..", "Resources", "budget_data.csv")

total_months = []
total_profit = []
Average_change = []
Monthly_profit = []

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
#skips column name https://evanhahn.com/python-skip-header-csv-reader/
    skip_header = next(csv_reader)
    #end here
    
    for row in csv_reader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))
    #end here

    #https://careerkarma.com/blog/python-typeerror-list-object-cannot-be-interpreted-as-an-integer/
    for i in range(len(total_profit)-1):#https://blog.finxter.com/python-indexerror-list-index-out-of-range/#:~:text=The%20error%20%E2%80%9Clist%20index%20out,index%20is%20out%20of%20range.
        Average_change.append(total_profit[i+1]-total_profit[i]) 
        #end code
    Month_max = max(Average_change)
    Month_min = min(Average_change)

    max_formonth = Average_change.index(max(Average_change))+1#https://www.w3schools.com/python/ref_list_index.asp
    min_formonth = Average_change.index(min(Average_change))+1




print(f"total months:{len(total_months)}")
print(f"total profit:{sum(total_profit)}")
print(f"Average Change:{round(sum(Average_change)/len(Average_change),2)}")
print(f"Greatest Increase in profits:{total_months[ max_formonth]},(${Month_max})")
print(f"Greatest Increase in profits:{total_months[ min_formonth]},(${Month_min})")


#end code





