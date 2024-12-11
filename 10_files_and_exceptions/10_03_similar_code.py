

from pathlib import Path

# Ask for the user's name
name = input("What's your name? ")

# Specify the file path
path = Path("guest.txt")

# Write the name to the file (it will create the file if it doesn't exist)
path.write_text(name)

# Confirm the name has been saved
print(f"Name '{name}' has been saved to guest.txt.")
