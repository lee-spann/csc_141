

# an empty list to store people in.
people = []

# define some people, and add them to the list.
person = {
    'first_name': 'lee',
    'last_name': 'spann',
    'age': 18,
    'city': 'reading',
    }
people.append(person)

person = {
    'first_name': 'lawrence',
    'last_name': 'spann',
    'age': 53,
    'city': 'easton',
    }
people.append(person)

person = {
    'first_name': 'diana',
    'last_name': 'polanco',
    'age': 18,
    'city': 'easton',
    }
people.append(person)

# display all of the information in the dictionary.
for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()

    print(f"{name}, of {city}, is {age} years old.")