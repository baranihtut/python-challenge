import csv

load = "budget_data.csv"
output_export = "budget_analysis1.txt"

month_total = 0
prev_rev = 0
month_of_change = []
changeList = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_rev = 0

with open(load) as rev_data:
    reader = csv.DictReader(rev_data)

    for row in reader:

        month_total = month_total + 1        
        total_rev = total_rev + int(row["Profit/Losses"])

        change = int(row["Profit/Losses"]) - prev_rev
        prev_rev = int(row["Profit/Losses"])
        changeList = changeList + [change]
        month_of_change = month_of_change + [row["Date"]]

        if change > greatest_increase[1]:
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = change

        if change < greatest_decrease[1]:
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = change

rev_avg = sum(changeList) / len(changeList)

output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {month_total}\n"
    f"Total: ${total_rev}\n"
    f"Average  Change: ${rev_avg}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

print(output)

with open(output_export, "w") as txt_file:
    txt_file.write(output)
