
# Used 4 spaces for indentation.
# Ensured consistent spacing around the code for readability.

flavors = ['pepperoni', 'bacon', 'mushroom']

for flavor in flavors:
    print(flavor)

print("\n")

for flavor in flavors:
    print(f"I really love {flavor} pizza!")

print("\nI really love pizza!")


#Removed the space between range and the parentheses.
#Added a space around the ** operator for clarity.
#Indented the lines inside the loops to ensure proper formatting.
cubes = []

for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)

for cube in cubes:
    print(cube)




#Removed the trailing commas in the pizza lists.
#Ensured consistent indentation for the print statements inside the loops.
#Removed unnecessary blank lines for cleaner formatting.
friend_pizzas = ['pepperoni', 'bacon', 'mushroom']

pizzas = ['pepperoni', 'bacon', 'mushroom']

friend_pizzas = pizzas[:]
pizzas.append('supreme')

friend_pizzas.append('peppers')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
