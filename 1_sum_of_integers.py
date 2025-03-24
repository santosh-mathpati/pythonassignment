# Function to calculate sum of n integers
def sum_of_n_numbers(n):
    total = 0
    for i in range(n):
        num = int(input(f"Enter number {i+1}: "))
        total += num
    return total

# Taking input from user
n = int(input("Enter the number of integers: "))

# Calculating sum
result = sum_of_n_numbers(n)

# Display result
print(f"The sum of {n} numbers is: {result}")
