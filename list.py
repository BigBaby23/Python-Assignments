my_list = []  # empty list

# Append elemrnt into empty list
my_list.extend([10, 20, 30, 40])

# Insert the value 15 at the second position (index 1)
my_list.insert(1, 15)

# Extend my_list with another list
my_list.extend([50, 60, 70])

# Remove the last element
my_list.pop()

# Sort my_list in ascending order
my_list.sort()

print(my_list)

#Find and print the index of the value 30 in my_list.
index_of_30 = my_list.index(30)
print(index_of_30)
