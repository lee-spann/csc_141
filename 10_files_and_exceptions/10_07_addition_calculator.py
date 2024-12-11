

from pathlib import Path

# Path to store the results
path = Path("calculator_results/calculations.txt")

# Create the folder if it doesn't exist
path.parent.mkdir(parents=True, exist_ok=True)

while True:
    try:
        num1 = input("Enter the first number (or 'quit' to stop): ")
        if num1.lower() == 'quit':
            break
        num1 = int(num1)

        num2 = input("Enter the second number (or 'quit' to stop): ")
        if num2.lower() == 'quit':
            break
        num2 = int(num2)

        result = num1 + num2
        print(f"The sum is: {result}")

        # Save the result to the file
        with path.open('a') as file:
            file.write(f"{num1} + {num2} = {result}\n")

    except ValueError:
        print("Please enter valid numbers.")
