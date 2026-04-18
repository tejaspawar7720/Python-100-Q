side1 = int(input("Enter Triangle first side: "))
side2 = int(input("Enter Triangle second side: "))
side3 = int(input("Enter Triangle third side: "))

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1 :
    print("All three side are Valid Triangle")
else:
    print("This is not a Valid Triangle Sides")