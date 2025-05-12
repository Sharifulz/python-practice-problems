### Problem-9: Find if 6 is available in the list 
#	my_list = [4, 8, 7, 4,3,6,2,1,9]

my_list = [4, 8, 7, 4,3,6,2,1,9]

print(my_list[:3])
print(my_list[2:5])
print(my_list[3:])
print(my_list[:-2])

for data in my_list:
    if data == 6:
        print("6 is available in the list!")
        break