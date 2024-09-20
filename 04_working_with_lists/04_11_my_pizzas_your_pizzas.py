

friend_pizzas = ['pepperoni', 'bacon', 'mushroom',]

pizzas = ['pepperoni', 'bacon', 'mushroom',]


friend_pizzas = pizzas[:]
pizzas.append('supreme')

friend_pizzas.append('peppers')
print("My favorite pizzas are:")
for pizza in pizzas:
 print(pizza)
	
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)
