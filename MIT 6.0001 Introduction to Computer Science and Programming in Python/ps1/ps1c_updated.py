starting_salary = float(input("Enter the starting salary: ")) #input starting salary
total_cost = 1000000
portion_down_payment = 0.25*total_cost
epsilon = 100
current_savings = 0
steps = 0
months = 0
r = 0.04 #annual return rate

low = 0
high = 10000
portion_saved = (low+high)/2 #portion saved



while True:
    months = 0
    current_savings = 0
    adjusted_salary = starting_salary
    portion_saved = (low + high)/2

    for months in range(0,37):
        monthly_salary = (adjusted_salary/12)
        current_savings = current_savings + current_savings*(r/12) + monthly_salary*(portion_saved/10000)
        
        if months%6 == 0: #adjusts salary to acount for raise
            adjusted_salary = adjusted_salary + adjusted_salary*0.07 #semi annual raise is 7%    
  
    if abs(current_savings - portion_down_payment) <= epsilon:
        print("Best savings rate: ", portion_saved/10000)
        print("Steps in bisection search:", steps)
        break
    
    if abs(current_savings - portion_down_payment) >= epsilon and current_savings < portion_down_payment:
        low = portion_saved
        
    elif abs(current_savings - portion_down_payment) >= epsilon and current_savings > portion_down_payment:
        high = portion_saved
            
    if portion_saved >= 10000:
        print("It is not possible to pay the down payment in three years.")
        break
    
    steps += 1
    