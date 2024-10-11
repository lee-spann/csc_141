

people = input("How many people are in your dinner group?:")
people = int(people)

if people > 8:
    print("\nYou'll have to wait for an available table.")
else:
    print("\nWe have a table available for you!")