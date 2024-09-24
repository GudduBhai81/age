# Program to check if age is between 10 and 20 years using nested conditionals
age = int(input("Enter your age: "))

if age >= 10:
    if age <= 20:
        print("The age is between 10 and 20 years.")
    else:
        print("The age is greater than 20.")
else:
    print("The age is less than 10.")