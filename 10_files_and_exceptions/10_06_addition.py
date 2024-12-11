

from pathlib import Path

# Ask for two numbers and display the sum
path = Path("addition_results/results.txt")

# Create the folder if it doesn't exist
path.parent.mkdir(parents=True, exist_ok=True)

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 + num2
    print(f"The sum is: {result}")

    # Save the result to the file
    with path.open('a') as file:
        file.write(f"{num1} + {num2} = {result}\n")
except ValueError:
    print("Please enter valid numbers.")
