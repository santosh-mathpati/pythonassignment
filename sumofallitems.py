#Write a program to Find the sum of all items in a dictionary,Set, Tuple ,List

# Define data structures
numbers_list = [1, 2, 3, 4, 5]
numbers_tuple = (1, 2, 3, 4, 5)
numbers_set = {1, 2, 3, 4, 5}
numbers_dict = {"a": 10, "b": 20, "c": 30}

# Calculate sum for each data structure
sum_list = sum(numbers_list)
sum_tuple = sum(numbers_tuple)
sum_set = sum(numbers_set)
sum_dict = sum(numbers_dict.values())  # Summing dictionary values

# Print results
print("Sum of List:", sum_list)
print("Sum of Tuple:", sum_tuple)
print("Sum of Set:", sum_set)
print("Sum of Dictionary Values:", sum_dict)
