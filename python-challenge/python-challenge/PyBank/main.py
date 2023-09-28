import csv

#list the path to the CSV file
csv_file_path = '/Users/laurenpescarus_razeware/Desktop/MSU Course/Classwork/python-challenge/python-challenge/PyBank/Resources/budget_data.csv'

#outline variables to store financial analysis data
total_months = 0
profitloss_net = 0
previous_profitloss = None
profitloss_changes = []
months = []

#open and read the CSV file
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    
    #skip the header row
    header = next(csv_reader)
    
    #create the output file path
    output_file_path = '/Users/laurenpescarus_razeware/Desktop/MSU Course/Classwork/python-challenge/python-challenge/PyBank/Analysis/output.txt'

    for row in csv_reader:
        #get data from the current row
        date = row[0]
        profitloss = int(row[1])  #convert profit/loss to an integer

        #calculate the total profit/loss over all months
        profitloss_net += profitloss

        #calculate profit/loss changes
        if previous_profitloss is not None:
            profitloss_change = profitloss - previous_profitloss
            profitloss_changes.append(profitloss_change)
            months.append(date)

        #update previous profit/loss for the next run
        previous_profitloss = profitloss

#math the total number of months
total_months = len(months)

#math the average change in profit/loss
average_change = sum(profitloss_changes) / len(profitloss_changes)

#find the greatest increase and decrease in profit/loss
max_increase = max(profitloss_changes)
max_decrease = min(profitloss_changes)

#match the months for the greatest increase and decrease
increase_month = months[profitloss_changes.index(max_increase)]
decrease_month = months[profitloss_changes.index(max_decrease)]

#create the output text
output_text = f"Financial Analysis" \
              f"----------------------------" \
              f"Total Months: {total_months}" \
              f"Total: ${profitloss_net}" \
              f"Average Change: ${average_change:.2f}" \
              f"Greatest Increase in Profits: {increase_month} (${max_increase})" \
              f"Greatest Decrease in Profits: {decrease_month} (${max_decrease})"

#write the output to a text file
with open(output_file_path, 'w') as output_file:
    output_file.write(output_text)

#display the results in the terminal
print(output_text)