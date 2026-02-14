"""
question 6
part 2: Arithmetic operations
"""

# Step 1 (input)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Step 2 (operations)
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2  

#  modulus and exponent
mod = num1 % num2 #  modulus
exp = num1 ** num2 # exponent

# Step 3 (reults)
print(f"{num1} + {num2} = {add}")
print(f"{num1} - {num2} = {sub}")
print(f"{num1} * {num2} = {mul}")
print(f"{num1} / {num2} = {div}")
print(f"{num1} % {num2} = {mod}")
print(f"{num1} ** {num2} = {exp}")
