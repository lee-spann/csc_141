

from pathlib import Path

# Ask why they like programming and save responses to a file
path = Path("programming_poll/programming_poll.txt")

# Create the folder if it doesn't exist
path.parent.mkdir(parents=True, exist_ok=True)

while True:
    reason = input("Why do you like programming? (or 'quit' to stop): ")
    if reason.lower() == 'quit':
        break
    with path.open('a') as file:
        file.write(f"{reason}\n")
    print("Thank you for your response!")
