


prompt = "\nWhat is your age?:"
prompt += "\n(Enter 'quit' when you are finished.): "

# Active variable to control the loop
active = True

while active:
    age = input(prompt)

    # Conditional test to stop the loop if 'quit' is entered
    if age == 'quit':
        break
    
    # Convert age to an integer and handle ticket price logic
    try:
        age = int(age)

        if age < 3:
            print("Your ticket is free")
        elif age < 13:
            print("Your ticket is $10")
        else:
            print("Your ticket is $15")
    
    except ValueError:
        print("Please enter a valid age or 'quit' to exit.")
