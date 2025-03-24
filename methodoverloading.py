# write a program to demonstrate Method overloading
class MathOperations:
    def add(self, a, b=0, c=0):  # Default arguments allow overloading
        return a + b + c

# Creating object
math_obj = MathOperations()

# Calling the method with different numbers of arguments

print("Sum of two numbers:", math_obj.add(5, 10))       # Uses two arguments
print("Sum of three numbers:", math_obj.add(5, 10, 15)) # Uses three arguments
