# WAP to Add, Delete, Discard and Update value in dictionary 
# Creating a dictionary
data = {}

# Adding values
data["name"] = "santosh"
data["age"] = 65
data["grade"] = "A"
print("After Adding:", data)

# Updating a value
data["age"] = 80
print("After Updating:", data)

# Deleting a value
del data["age"]
print("After Deleting:", data)

# Discarding a value
data.pop("grade")  # 
print("After Discarding:", data)

