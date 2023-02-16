# This is a Python program. 
# The user provides what type of investment he wants and then other parameteres like initial amount, number of years and rate of interest.
# The program then outputs the total amount that the user will earn

import math

print("Choose either 'investment' or 'bond' from the menu below to proceed:\n")

print("Investment - to calculate the amount of interest you'll earn on your investment")

print("bond - to calculate the amount you'll have to pay on a home loan\n")

user_selected = input("Pls select one: ")
# In this if block , we compute amount for the BOND 
if (user_selected.upper() == "BOND"):   
   house_value = float(input("\nenter the value of the house: "))
   interst_rate = float(input("pls enter the intrest rate: "))
   number_months = int(input("pls enter number of months repaid: "))
   interst_rate = (interst_rate / 12) / 100   
   total_amount = (interst_rate * house_value)  / (1 - ((1 + interst_rate)**(-number_months) ))
   print(f"\nYou will earn back the following amount: {round(total_amount,2)}")
  
  # In this else block, we compute amount for the  INVESTMENT 
elif (user_selected.upper() == "INVESTMENT"):   
   amount = float(input("\nenter the amount you are depositing: "))
   intrest_rate = float(input("pls enter the interst rate: "))
   intrest_rate = intrest_rate / 100
   number_year = float(input("enter the number of years: "))
   
   interst_type = input("pls select the interst type: ")
   if (interst_type.upper() == "SIMPLE"):     
     total_amount = 0
     total_amount = amount*(1 + intrest_rate * number_year)
   else:     
     total_amount = amount * math.pow((1+intrest_rate),number_year)     
   
   print(f"\nThe total amount you earn is {round(total_amount,2)} ") 
else:
   print("wrong selection")


  
  

