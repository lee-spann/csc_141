


import json
from pathlib import Path

# Path to the saved favorite number
path = Path("favorites/favorite_number.json")

# Create the folder if it doesn't exist
path.parent.mkdir(parents=True, exist_ok=True)

# Retrieve and display the stored favorite number
if path.exists():
    with path.open() as file:
        number = json.load(file)
    print(f"Your favorite number is {number}.")
else:
    print("I don't know your favorite number yet.")
