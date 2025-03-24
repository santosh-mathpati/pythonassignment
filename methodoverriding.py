class Parent:
    def show(self):
        print("This is the Parent class.")

class Child(Parent):
    def show(self):  # Overriding the Parent class method
        print("This is the Child class.")

# Creating objects
parent_obj = Parent()
child_obj = Child()

# Calling the methods
parent_obj.show()  # Calls Parent class method
child_obj.show()   # Calls overridden Child class method
