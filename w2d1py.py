

# initial declarations


portion_down_payment = 0.25
current_savings = 0
annual_rate = 0.04
r = 12
current_savings = 0 
m = 0

print("First, a few questions:")
annual_salary = float(input("What is your annual salary?"))
monthly_salary = float(annual_salary) / int(r)
print("So your monthly salaray is "+ str(monthly_salary))
total_cost = float(input("Next, what is the cost of your dream home?"))
print ("...and you have in mind a dream home that will cost $" + str(total_cost))
downpayment = portion_down_payment * total_cost
print ("The amount you will need for downpayment is $" + str(downpayment))
portion_saved = float(input("And what percent of your paycheck do you want to save everytime? "))
print ("which you want to achieve by setting aside " + str(portion_saved) + " of your pacheck")
m = 0



while current_savings < downpayment: 
    if m == 0:
        current_savings = portion_saved * monthly_salary
    else:
        current_savings = (portion_saved * monthly_salary) + (current_savings * (1 + (annual_rate/r)))    
    m += 1
    print ("After " + str(m) + " months, your savings is $"+ str(current_savings))