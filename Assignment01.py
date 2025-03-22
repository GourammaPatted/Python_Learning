#01 Write a Program for sum of n integers number
n = int(input("Enter the number of integers: "))
total = 0
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    total += num
print("Sum of the given numbers:", total)

#02 Write sum of integers in list
numbers = [5, 10, 15, 20,53,1]
total = sum(numbers)
print("Sum of the given numbers:", total)

#03 Write program to store value in dictionary
my_dict = {}
#key-value pairs
my_dict["name"] = "Alex"
my_dict["age"] = 25
my_dict["city"] = "Delhi"
my_dict["email"] = "alex.gmail"

print("Stored Dictionary:", my_dict)

#04 Write program to Add, Delete, Discard and Update value in dictionary
# Adding a new key-value pair
my_dict["country"] = "India"

# Updating a value
my_dict["age"] = 29 

# Deleting a key-value pair
del my_dict["city"]

# Discarding/Removing a key
my_dict.pop("name", None)
print("Dictionary after discarding 'name':", my_dict)

#05 Write program to store value and perform basic operation like unioun, interaction in Set
set1 = {11, 12, 13, 24, 15}
set2 = {14, 15, 16, 27, 18}

#union will combine both sets
union_set = set1 | set2 
# union_set = set1.union(set2)
print("Union:", union_set)

#intersection will give common elements in both sets
intersection_set = set1 & set2  
# intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

#difference will give elements which are in set1 but not in set2
difference_set = set1 - set2 
 # difference_set = set1.difference(set2)
print("Difference (set1 - set2):", difference_set)

#union - intersection
symmetric_difference_set = set1 ^ set2  
# symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference_set)


#06 Write program to validate age using if and else
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age! Age cannot be negative.")
elif age < 18:
    print("You are a minor.")
elif age >= 18 and age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


#07 Write program to reverse a string
text = "selenium"
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print("reversed string - "+reversed_text)

#08 Find the sum of all items in a dictionary,Set, Tuple ,List
# 01 - Dictionary
my_dict = {1: 10, 2: 20, 3: 30}
# Sum of dictionary only values
dict_sum = sum(my_dict.values())
print("Sum of dictionary values:", dict_sum)
# Sum of dictionary keys and values
total_sum = sum(my_dict.keys()) + sum(my_dict.values())
print("Sum of both keys and values:", total_sum)

# 02 - Set
my_set = {1, 2, 3, 4, 5}
# Sum of set elements
set_sum = sum(my_set)
print("Sum of set elements:", set_sum)

# 03 - Tuple
my_tuple = (1, 2, 3, 4, 5)
# Sum of tuple elements
tuple_sum = sum(my_tuple)
print("Sum of tuple elements:", tuple_sum)

# 04 - List
my_list = [1, 2, 3, 4, 5]
# Sum of list elements
list_sum = sum(my_list)
print("Sum of list elements:", list_sum)

#09 Write program to find the largest and smallest number in a list
# Method Overloading using *args
class Calculator:
    def add(self, *args):  # Accepts variable number of arguments
        return sum(args)  # Sums all provided numbers

# Method Overriding Example
class Parent:
    def show(self):
        print("This is the Parent class.")

class Child(Parent):
    def show(self):  # Overriding the Parent class method
        print("This is the Child class.")

# Testing Method Overloading
calc = Calculator()
print("Sum with 1 arg:", calc.add(10))            
print("Sum with 2 args:", calc.add(10, 20))       
print("Sum with 3 args:", calc.add(10, 20, 30))  
print("Sum with 5 args:", calc.add(1, 2, 3, 4, 5)) 

# Testing Method Overriding
p = Parent()
p.show() 

c = Child()
c.show() 

#10 Write One Exception Handling program
try:
    # Taking input and converting to integer
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Performing division
    result = num1 / num2  
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Invalid input! Please enter numbers only.")

except Exception as e:
    print(f"Unexpected error: {e}")

finally:
    print("Execution completed. Thank you!")

#11 Write Program for oops concept
from abc import ABC, abstractmethod  # Importing for abstraction

# Class and Object Example
class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand  
        self.model = model 
 # Private attribute (Encapsulation)
        self.__price = price  
    # Getter for private attribute
    def get_price(self): 
        return self.__price
    # Setter for private attribute
    def set_price(self, price):  
        if price > 0:
            self.__price = price
        else:
            print("Invalid price!")

    def show_details(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: {self.__price}"

# Inheritance Example
class Car(Vehicle):
    def __init__(self, brand, model, price, fuel_type):
        super().__init__(brand, model, price)  # Call parent constructor
        self.fuel_type = fuel_type

# Method Overriding (Polymorphism)
    def show_details(self): 
        return f"{super().show_details()}, Fuel Type: {self.fuel_type}"

# Abstraction Example
class Bike(ABC):  # Abstract class
    @abstractmethod
    def bike_type(self):
        pass

class SportsBike(Bike):
    def bike_type(self):
        return "This is a Sports Bike."

# Creating an object of Vehicle
v1 = Vehicle("Toyota", "Corolla", 25000)
print(v1.show_details())

# Accessing Encapsulation (Private Variable)
print("Original Price:", v1.get_price())  
v1.set_price(27000)  # Updating price
print("Updated Price:", v1.get_price())

# Creating an object of Car (Inheritance & Polymorphism)
c1 = Car("Honda", "Civic", 30000, "Petrol")
print(c1.show_details()) 

# Creating an object of SportsBike (Abstraction)
bike = SportsBike()
print(bike.bike_type())


