income = int(input("Enter Your annual income to Calculate Tax: "))

if income >= 0  and income <= 400000:
    print("Your income Tax will be Nill ")

elif income >= 400000  and income <= 800000:
    payble = income * (5 / 100)
    print("Your income Tax will be 5% So total Payble tax is : " ,payble)
    
elif income >= 800000  and income <= 1200000:
    payble = income * (10 / 100)
    print("Your income Tax will be 10% So total Payble tax is : ", payble)
    
elif income >= 1200000  and income <= 1600000:
    payble = income * (15 / 100)
    print("Your income Tax will be 15% So total Payble tax is: ", payble)

elif income >= 1600000  and income <= 2000000:
    payble = income * (20 / 100)
    print("Your income Tax will be 20% So total Payble tax is: ", payble)

elif income >= 2000000  and income <= 2400000:
    payble = income * (25 / 100)
    print("Your income Tax will be 25% So total Payble tax is: ", payble)
else:
    payble = income * (30 / 100)
    print("Your income tax be 30% So total payble tax is : ",payble)