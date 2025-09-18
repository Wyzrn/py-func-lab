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