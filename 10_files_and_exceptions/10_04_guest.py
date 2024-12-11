


from pathlib import Path

# Ask for guest names and store them in a file
path = Path("guest_book/guest_book.txt")

# Create the folder if it doesn't exist
path.parent.mkdir(parents=True, exist_ok=True)

while True:
    name = input("Enter your name (or 'quit' to stop): ")
    if name.lower() == 'quit':
        break
    with path.open('a') as file:
        file.write(f"{name}\n")
    print(f"Welcome, {name}!")
