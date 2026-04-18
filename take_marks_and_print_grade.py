marks = int(input("Enter the marks : "))

if marks >= 90 :
    print("Your Grade is A")
elif marks <= 90 and marks >= 80:
    print("Your Grade is B")
elif marks <= 80 and marks >= 70:
    print("Your Grade is C")
elif marks <= 70 and marks >= 60:
    print("Your Grade is D ")
else:
    print("Your grade is F ")