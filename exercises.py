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