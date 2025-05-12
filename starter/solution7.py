### Problem-7: Write a function that takes 1 number as argument. The function should return “Fizz” 
# if the number is divisible by 3, the function should return “Buzz” if the number is divisible by 5, 
# the function should return “FizzBuzz” if the number is divisible by both 5 and 3, otherwise return “Not a Fizz-buzz number”
#	Hints: Use condition inside the function

number=int(input("Enter any number:"))

if number%3==0 and number%5==0:
    print("FizzBuzz")
elif number%3==0:
    print("Fizz")
elif number%5==0:
    print("Buzz")
else:
    print("Not a FizzBuzz number!")