
from pathlib import Path

# Read the file
path = Path("learning_python.txt")
contents = path.read_text().strip()

# Print each line
for line in contents.splitlines():
    print(line)







