

prompt = "\nPlease enter the topping you want on your pizza:"

prompt += "\n(Enter 'quit' when you are finished.):"

while True:
    topping = input(prompt)

    if topping != 'quit':
        break
    
    else:
        print(f"Ok I'll add the {topping} to your pizza!")