


from pathlib import Path

# Path to the text file
path = Path("text_files/text_file.txt")

# Create the folder if it doesn't exist
path.parent.mkdir(parents=True, exist_ok=True)

try:
    # Try to read the file, if it exists
    contents = path.read_text().lower()
    word = "the"
    count = contents.count(word)
    print(f"The word '{word}' appears {count} times.")
except FileNotFoundError:
    # If the file doesn't exist, create it with default content
    print("text_file.txt not found. Creating the file with default content.")
    with path.open('w') as file:
        file.write("There is no book")
    
    # Read and count again after creating the file
    contents = path.read_text().lower()
    word = "the"
    count = contents.count(word)
    print(f"The word '{word}' appears {count} times.")

