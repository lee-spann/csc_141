


from pathlib import Path

# Files for cat and dog names
files = ["cats.txt", "dogs.txt"]
for file_name in files:
    path = Path(f"pets/{file_name}")

    # Create the folder if it doesn't exist
    path.parent.mkdir(parents=True, exist_ok=True)

    try:
        # Try to read the file, if it exists
        contents = path.read_text().strip()
        print(f"{file_name} contents:\n{contents}")
    except FileNotFoundError:
        # If the file doesn't exist, silently create it with default content
        with path.open('w') as file:
            if file_name == "cats.txt":
                file.write("Luna\nBella\nOliver\n")
            elif file_name == "dogs.txt":
                file.write("Max\nCharlie\nBuddy\n")


