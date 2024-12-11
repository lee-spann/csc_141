


import json
from pathlib import Path

# Path to save favorite number
path = Path("favorites/favorite_number.json")

# Create the folder if it doesn't exist
path.parent.mkdir(parents=True, exist_ok=True)

# Ask for the favorite number and save it to the file
number = input("What's your favorite number? ")
with path.open('w') as file:
    json.dump(number, file)
print("Your favorite number has been saved!")
