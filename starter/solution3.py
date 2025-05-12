### Problem-3: Write a function that takes 2 numbers as arguments (age of two brothers) and find who is elder
#	Hints: Use condition inside the function

brother1Age=input("Enter brother 1 age: ")
brother2Age=input("Enter brother 2 age: ")

print("Brother 1 age is: ", brother1Age, ", Brother 2 age is: ", brother2Age)

if brother1Age>brother2Age:
    print("Brother 1 is the elder one.")
else:
    print("Brother 2 is the elder one.")