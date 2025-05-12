### Problem-8: Guessing game

# Write a function that takes a number 1 to 9 from the user input (use input function inside a function). 
# Store a number in a variable (let’s assume 6). If the input value is less than the variable, 
# print (your guess is almost there), 
# if the input value is greater than the variable, print - your guess is higher, 
# if the input value and variable are equals, print - Your Guess Is Correct!

num = int(input("Enter any number between 1 to 10:"))
expectedValue = 6

if num<1 or num>9:
    print("Given number is not between 1-10. Can not proceed.")
else:
    if num==expectedValue:
        print("Your Guess Is Correct!")
    elif num < expectedValue:
        print("Your guess is almost there")
    else:
        print("Your guess is higher")