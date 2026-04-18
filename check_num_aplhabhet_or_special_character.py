char = input("Enter a character :" )
if char.isdigit() :
    print(char,": is digit")
elif char.isalpha():
    print(char,"is Alphabet ")
else:
    print(char,": is special character ")
