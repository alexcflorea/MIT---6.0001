#Input Variables

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:  "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semiannual raise, as a decimal: "))

#Global Variables
portion_down_payment = 0.25 #the calculator calculates how long it will take to pay the down payment NOT the total cost
current_savings = float(0)
r = 0.04 #anual return rate
monthly_salary = (annual_salary/12)
months = 0

while current_savings <= (total_cost*portion_down_payment):
    current_savings = current_savings*(1+r/12) + monthly_salary*portion_saved
    
    if months%6 == 0 and months != 0: #adjusts salary to acount for raise
        annual_salary = annual_salary*(1 + semi_annual_raise)
        monthly_salary = (annual_salary/12)
    
    
    months += 1
    
print("Number of months: ", months)