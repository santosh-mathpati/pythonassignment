# Write program to validate age using if and else

age = int(input("Enter your age: "))
if age < 0:
    print("Invalid age! Age cannot be negative.")
elif age < 18:
    print("You are a minor.")
elif age >= 18 and age <= 100:
    print("You are an adult.")
else:
    print("Invalid age! Please enter a realistic age.")
