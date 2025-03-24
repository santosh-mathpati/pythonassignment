# Write One Exception Handling program
try:
    # Taking user input
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Performing division (which may raise an exception)
    result = num1 / num2  

    # Printing the result
    print("Result:", result)

# Handling division by zero error
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Handling invalid input (non-integer values)
except ValueError:
    print("Error: Invalid input! Please enter numeric values.")

# Handling any other unexpected error
except Exception as e:
    print("An unexpected error occurred:", e)

# Finally block executes no matter what
finally:
    print("Execution completed.")
