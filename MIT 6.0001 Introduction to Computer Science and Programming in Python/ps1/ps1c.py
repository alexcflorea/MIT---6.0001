starting_salary = float(input("Enter the starting salary: ")) #input starting salary
total_cost = 1000000
portion_down_payment = 0.25*total_cost
epsilon = 100
current_savings = 0
steps = 0
months = 0

low = 0
high = 10000
r = (low+high)/2 #portion saved



while abs(current_savings - portion_down_payment) >= epsilon:
    months = 0
    current_savings = 0
    adjusted_salary = starting_salary
    r = (low + high)/2

    for months in range (0,36):
        monthly_salary = (adjusted_salary/12)
        current_savings = current_savings + current_savings*(0.04/12) + monthly_salary*(r/10000)
        
        if months%6 == 0: #adjusts salary to acount for raise
            adjusted_salary = adjusted_salary + adjusted_salary*0.07 #semi annual raise is 7%    
  
    if abs(current_savings - portion_down_payment) >= epsilon and current_savings < portion_down_payment:
        low = r
        
    elif abs(current_savings - portion_down_payment) >= epsilon and current_savings > portion_down_payment:
        high = r
    
    
    steps += 1
        
    if r >= 10000:
        print("It is not possible to pay the down payment in three years.")
        break

else:
    print("Best savings rate: ", r/10000)
    print("Steps in bisection search:", steps)