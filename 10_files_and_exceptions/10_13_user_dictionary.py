


import json
from pathlib import Path

# Path to the saved favorite number
path = Path("favorites/favorite_number.json")

# Create the folder if it doesn't exist
path.parent.mkdir(parents=True, exist_ok=True)

# Verify and update the favorite number
if path.exists():
    with path.open() as file:
        number = json.load(file)
    confirm = input(f"Is {number} still your favorite number? (yes/no): ")
    if confirm.lower() == 'no':
        new_number = input("What's your new favorite number? ")
        with path.open('w') as file:
            json.dump(new_number, file)
        print("Your favorite number has been updated!")
else:
    number = input("What's your favorite number? ")
    with path.open('w') as file:
        json.dump(number, file)
    print("Your favorite number has been saved!")
