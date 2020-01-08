import os
import csv

Data_csv = os.path.join("Resources", "budget_data.csv")


with open(Data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)
    
    Data = [row for row in csvreader]
    
    months = int(sum(1 for row in Data))
    
    NetAmount = 0
    for row in Data:
        amount = float(row[1])
        NetAmount = NetAmount + amount
    NetAmount= int(NetAmount)
    
    TotalChange = 0
    ChangeList = []
    for i in range(months-1):
        row = Data[i]
        ThisMonthAmount = float(row[1])
        NextRow = Data[i+1]
        NextMonthAmount = float(NextRow[1])
        Change = NextMonthAmount-ThisMonthAmount
        TotalChange = TotalChange + (NextMonthAmount-ThisMonthAmount)
        ChangeList.append(Change)
    MaxIndex = ChangeList.index(max(ChangeList))
    MaxRow = Data[MaxIndex+1]
    MaxMonth= MaxRow[0]
    MinIndex = ChangeList.index(min(ChangeList))
    MinRow = Data[MinIndex+1]
    MinMonth = MinRow[0]
    MaxChangeList= int(max(ChangeList))
    MinChangeList= int(min(ChangeList))

    print("Financial Analysis")
    print("----------------------------------")
   
    print("Total Months: " + str(months))
    print("Total: " + "$"+str(NetAmount))
    print("Average Change: " + "$" + '{0:.2f}'.format(TotalChange/(months-1)))
    print("Greatest Increase in Profits: " + MaxMonth + " " + "($" + str(MaxChangeList) + ")")
    print("Greatest Decrease in Profits: " + MinMonth + " " + "($"+ str(MinChangeList) + ")")
       
    
    
    with open("Financial_Analysis","w") as file:

    
        file.write("Financial Analysis")
        file.write("\n")
        file.write("----------------------------------")
        file.write("\n")
        file.write("Total Months: " + str(months))
        file.write("\n")
        file.write("Total: " + "$"+str(NetAmount))
        file.write("\n")
        file.write("Average Change: " + "$" + '{0:.2f}'.format(TotalChange/(months-1)))
        file.write("\n")
        file.write("Greatest Increase in Profits: " + MaxMonth + " " + "($" + str(MaxChangeList) + ")")
        file.write("\n")
        file.write("Greatest Decrease in Profits: " + MinMonth + " " + "($"+ str(MinChangeList) + ")")
        file.write("\n")
       
    
    
    
    
    
    