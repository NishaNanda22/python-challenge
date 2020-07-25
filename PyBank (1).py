#!/usr/bin/env python
# coding: utf-8

# In[16]:


import csv
import os

with open('03-Python_homework_assignment_PyBank_Resources_budget_data.csv') as csvfile:
    readCSV = csv.reader(bank_data)
    for row in readCSV:

# removed header in the file
# i cant figure out the syntax
                month_of_change = []
                net_change = []
                great_dec = ["", 9999999999]
                great_inc = ["", 0]
                number_of_months = 0
                net_profits = 0


                                                    # Track the net change
                net_change = int(row[1]) - prev_net
                prev_net = int(row[1])
                net_change = net_change + [net_change]
                month_of_change = month_of_change + [row[0]]

                if net_change < great_dec[1]:
                    great_dec[0] = row[0]
                    great_dec[1] = net_change

                                                    # Calculate the greatest increase
                if net_change > greatest_inc[1]:
                    great_inc[0] = row[0]
                    great_inc[1] = net_change



                                                # Calculate the Average Net Change
                net_monthly_avg = sum(net_change) / len(net_change)

                number_of_months = number_of_months + 1
                net_profits = net_profits + int(row[1])

#results
results = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Number of Months: {number_of_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase: {great_inc[0]} (${great_inc[1]})\n"
    f"Greatest Decrease: {great_dec[0]} (${great_dec[1]})\n")

print(results)

with open(file_to_output, "w") as txt_file:
    txt_file.write(results)


# In[33]:


import csv
import os

with open('03-Python_homework_assignment_PyBank_Resources_budget_data.csv') as bank_data:
    readCSV = csv.reader(bank_data)
    for row in readCSV:

# removed header in the file
# cant figure out how to declare increase and decrease

                month_of_change = []
                net_list = int(row([1])
                decrease = [-999999999,999999999]
                increase = [999999999, -999999999]
                number_of_months = 0
                net_profits = 0
                
                #something is wrong here?
                
                net_list = net_list + [net_list]
                month_of_change = month_of_change + [row[0]]

                if net_change < decrease[1]:
                    decrease[0] = row[0]
                    decrease[1] = net_change
                                                   
                if net_change > great_inc[1]:
                    increase[0] = row[0]
                    increase[1] = net_change
                                
                net_monthly_avg = sum(net_change) / len(net_change)

                number_of_months = number_of_months + 1
                net_profits = net_profits + int(row[1])

#results
results = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Number of Months: {number_of_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase: {increase[0]} (${increase[1]})\n"
    f"Greatest Decrease: {decrease[0]} (${decrease[1]})\n")

print(results)

with open(file_to_output, "w") as txt_file:
    txt_file.write(results)


# In[ ]:




