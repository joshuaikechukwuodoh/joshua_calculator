import random

def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:  # Avoid division by zero
            return "Undefined (division by zero)"
        return round(num1 / num2, 2)  # Round result to 2 decimal places for clarity

# Generate random numbers and a random operation
num1 = random.randint(1, 11)
num2 = random.randint(55, 100)
operations = ["+", "-", "*", "/"]
operation = random.choice(operations)

# Print question
print(f"Question: {num1} {operation} {num2}")

# Calculate result
result = calculate(num1, num2, operation)

# Get user input and validate
try:
    user_answer = float(input("What is the answer? (round to 2 decimal places if needed):\n"))
    if result == user_answer:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is {result}")
except ValueError:
    print("Invalid input! Please enter a numeric value.")
