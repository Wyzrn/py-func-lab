# Exercise 1: Calculate Area of a Triangle
def calculate_area_triangle(base, height):
    area = (base * height) / 2
    return area

# Test the function
print('Exercise 1:', calculate_area_triangle(10, 5))

# Exercise 2: Calculate Simple Interest
def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

# Test the function
print('Exercise 2:', simple_interest(1000, 5, 2))

# Exercise 3: Apply a Discount
def apply_discount(price, discount):
    new_price = price * (1 - discount / 100)
    return new_price

# Test the function
print('Exercise 3:', apply_discount(100, 25))

# Exercise 4: Convert Temperature
def convert_temperature(temp, unit):
    if unit == 'C':
        return (temp * 9 / 5) + 32
    elif unit == 'F':
        return (temp - 32) * 5 / 9
    else:
        return None  # Invalid unit, but minimal handling

# Test the function
print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))

# Exercise 5: Sum to N
def sum_to(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Test the function
print('Exercise 5:', sum_to(6))

# Exercise 6: Find the Largest Number
def largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Test the function
print('Exercise 6:', largest(1, 2, 3))

# Exercise 7: Calculate a Tip
def calculate_tip(bill, tip_percent):
    tip = bill * (tip_percent / 100)
    return tip

# Test the function
print('Exercise 7:', calculate_tip(50, 20))

# Exercise 8: Calculate Product of Numbers
def product(*args):
    result = 1
    for num in args:
        result *= num
    return result

# Test the function
print('Exercise 8:', product(2, 5, 5))

# Exercise 9: Basic Calculator
def basic_calculator(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return None  # Avoid division by zero
    else:
        return None  # Invalid operation

# Test the function
print('Exercise 9 Result:', basic_calculator(10, 5, "subtract"))