

# an empty list to store the pets in.
pets = []

# individual pets, and store each one in the list.
pet = {
    'animal type': 'cat',
    'name': 'domy',
    'owner': 'diana',
    'weight': 4.5,
    'eats': 'cat food',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'princess',
    'owner': 'angie',
    'weight': 9,
    'eats': 'dog food',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'dolce',
    'owner': 'michaela',
    'weight': 3,
    'eats': 'shoes',
}
pets.append(pet)

# display information about each pet.
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")