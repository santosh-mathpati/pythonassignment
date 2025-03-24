#WAP to store value and perform basic operation like unioun, interaction in Set

# Creating sets
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

# Union: Combines all unique elements from both sets
union_set = setA.union(setB)
print("Union:", union_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection: Finds common elements in both sets
intersection_set = setA.intersection(setB)
print("Intersection:", intersection_set)  # Output: {4, 5}

# Difference: Elements in setA but not in setB
difference_set = setA.difference(setB)
print("Difference (A - B):", difference_set)  # Output: {1, 2, 3}

# Symmetric Difference: Elements in either setA or setB, but not both
symmetric_difference_set = setA.symmetric_difference(setB)
print("Symmetric Difference:", symmetric_difference_set)  # Output: {1, 2, 3, 6, 7, 8}