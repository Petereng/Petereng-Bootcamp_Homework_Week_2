from pathlib import Path
import csv

filepath = Path("./budget_data.csv")

count_of_months = 0
total_profit = 0
total_change = 0
last_profit = 0
greatest_profit = -99999999
greatest_loss = 99999999

greatest_profit_month = ""
greatest_loss_month = ""

with open(filepath, 'r') as file_content:
    
    data = csv.reader(file_content)
    print(str(type(data)))
    head = next(data)
#     print(head)
    for Row in data:
       
        Row[1] = int(Row[1])
        total_profit += Row[1]
        if count_of_months > 0:
            change = Row[1] - last_profit
            if change > greatest_profit:
                greatest_profit = change
                greatest_profit_month = Row[0]
            if change < greatest_loss:
                greatest_loss = change
                greatest_loss_month = Row[0]
                
            total_change += change
        
        count_of_months += 1
        last_profit = Row[1]
    
print(f'''
  Financial Analysis
  ----------------------------
  Total Months: {count_of_months}
  Total: ${total_profit:,.0f}
  Average  Change: ${total_change/count_of_months-1:,.02f}
  Greatest Increase in Profits: {greatest_profit_month} (${greatest_profit:,.0f})
  Greatest Decrease in Profits: {greatest_loss_month} (${greatest_loss:,.0f})
''')