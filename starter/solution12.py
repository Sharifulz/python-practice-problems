### Problem-12: Find the common items between the lists 
# and make SUM of the new list items which are common between the lists.
#	list1 = [3, 5, 7, 4, 8, 8]
#	list2 = [4, 9, 8, 7, 1, 1, 13]

list1 = [3, 5, 7, 4, 8, 8]
list2 = [4, 9, 8, 7, 1, 1, 13]

# Find unique common items
common = list(set(list1) & set(list2)) # & represnt intersection in set

# Sum of common items
total = sum(common)

print("Common items:", common)
print("Sum of common items:", total)
