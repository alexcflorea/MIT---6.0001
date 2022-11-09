#Input Variables

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:  "))
total_cost = float(input("Enter the cost of your dream home: "))

#Global Variables
portion_down_payment = 0.25
current_savings = float(0)
r = 0.04 #anual return rate
monthly_salary = (annual_salary/12)
months = 0

while current_savings <= (total_cost*portion_down_payment):
    current_savings = current_savings*(1+r/12) + monthly_salary*portion_saved
        
    months += 1
    
print("Number of months: ", months)
