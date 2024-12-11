


import json
from pathlib import Path

# Path to store numbers
path = Path("numbers_data/numbers.json")

# Create the folder if it doesn't exist
path.parent.mkdir(parents=True, exist_ok=True)

# Write numbers to a file
numbers = [1, 2, 3, 4, 5]
with path.open('w') as file:
    json.dump(numbers, file)

# Read numbers from the file
with path.open() as file:
    numbers = json.load(file)
print(f"Numbers: {numbers}")
