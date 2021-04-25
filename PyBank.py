# Create file paths across operating systems
import os
import csv
# pass/join individual sub components 
with open('budget_data.csv',encoding='ISO 8859-1') as csvfile:

#Create Function ('Bank_Analysis')

#define variables
count_of_months = 0
data_list= []
profit_net = 0
profit_delta = 0
total_profit_delta = 0
delta = 0
delta_list = 0
sum_profit = 0
sum_loss = 0
row_count = 0 
Avg_delta= 0 
first_delta = 0
preceding_month = 0
greatest_profit_increase
greatest_profit_decrease
increase_date= ''
decrease_date= ''

#initialize csv.writer
	csvreader = csv.reader(csvfile, delimiter=',')
#read header on row, append 
	csv_header= next(csvreader)
    for row in csv_reader:
        data_list.append(row) 

    for row in data_list:
             
        if first_delta == 0 :
        	preceding_month = int(row[1]) 
            row_count = row_count +1        
            first_delta = 1
            profit_net= profit_net + int(row[1])
        else :
            profit_net= profit_net + int(row[1])
            row_count = row_count +1 
            profit_delta = int(row[1]) - preceeding_month
            total_profit_delta = total_profit_delta + profit_delta
            preceeding_month = int(row[1])

    for row in data_list:
        if 	int(row[1]) > greatest_profit_increase : 
            greatest_profit_increase = int(row[1])
            increase_date = row[0], [0]
        elif int(row[1]) < greatest_profit_decrease:
        	greatest_profit_decrease = int(row[1])
            decrease_date = row[0], [0]

avg_delta = total_profit_delta/(row_count-1)


    #txtfile.write('Summary_Analysis')
    #txtfile.write('\n------------------------------------')
    #txtfile.write(f'\nTotal Months: {monthsCount}')   

#Result_of_Analysis =(f"Financial Analysis \n" f"--------------------\n" f"Total Months: {total_months} \n"
    # f"Total: ${round(total_amount)}\n"f"Avereage Change: ${round(average_change,2)}\n"f"Greatest Increase in Profits:  {max_change_date} (${round(greatest_increase_profit)})\n"
     #f"Greatest Decrease in Profits:  {min_change_date} (${round(greatest_decrease_profit)})\n")#monthly calculation
#write csv file/ Give path to save file
# = os.path.join("PyBankOutcome.txt")

#Write results into text file.
  # with open(bank_output, 'w+ as txtfile:
    

print ('Bank_Analysis')
print('------------------------------------')
print(f'count_of_months : {row count}')
print(f'average_change :{average_change}')
print(f'total : {sum_profit}')
print(f'greatest_profit_increase : {greatest_profit_increase}')
print(f'greatest_profit_decrease: {greatest_profit_decrease}') 
