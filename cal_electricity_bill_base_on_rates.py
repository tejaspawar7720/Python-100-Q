rate = 0.25
usage = int(input("Enter Your Total consumption unit : "))
 
if usage >=0:
    bill = usage * rate
    print(" Your Total Bill is : " , bill, "RS")
else:
    print("No Bill")