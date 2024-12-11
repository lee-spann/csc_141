

from pathlib import Path

# Path to the file
path = Path("learning_python.txt")

# Read the file and print each line with "Python" replaced by "C"
contents = path.read_text().strip()
for line in contents.splitlines():
    print(line.replace("Python", "C"))
