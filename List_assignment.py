# Step-by-step list operations with prints for verification

# 1. Create an empty list called my_list.
my_list = []
print("1) Start:", my_list)

# 2. Append the following elements to my_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("2) After appends:", my_list)

# 3. Insert the value 15 at the second position in the list.
my_list.insert(1, 15)  # index 1 is the second position
print("3) After insert 15 at index 1:", my_list)

# 4. Extend my_list with another list: [50, 60, 70].
my_list.extend([50, 60, 70])
print("4) After extend [50, 60, 70]:", my_list)

# 5. Remove the last element from my_list.
my_list.pop()  # removes 70
print("5) After removing last element:", my_list)

# 6. Sort my_list in ascending order.
my_list.sort()
print("6) After sort ascending:", my_list)

# 7. Find and print the index of the value 30 in my_list.
index_30 = my_list.index(30)
print(f"7) Index of 30: {index_30}")

# For clarity, final state:
print("Final list:", my_list)