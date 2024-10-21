

 # Using lists to race cars
import random
import os

# Clear the console (optional)
os.system('cls')

# Every car must have a speed ranking (representing how fast they can go)
cars = {'Ferrari': 220, 'Lamborghini': 230, 'Porsche': 210, 'Bugatti': 250, 'McLaren': 240}

number_of_cars = len(cars)

# Get a list of the car names and their top speeds
car_names = list(cars.keys())
car_speeds = list(cars.values())

print("The cars in the race are:")
for car in car_names:
    print(car)
print('\n')

# Set up your car's stats
your_speed = 225
your_max_boost = 15
your_handling = random.randint(1, 10)  # Random handling score between 1 and 10
your_luck = random.randint(1, 5)  # Random luck score between 1 and 5

print(f'Your car is a custom-built machine with a top speed of {your_speed} mph, handling score of {your_handling}, and a luck factor of {your_luck}!\n')

# Get a random car to race against
random_number = random.randint(0, number_of_cars - 1)
opponent_car = car_names[random_number]
opponent_speed = car_speeds[random_number]
opponent_handling = random.randint(1, 10)
opponent_luck = random.randint(1, 5)

print(f'You are set to race against the {opponent_car}, which has a top speed of {opponent_speed} mph, handling score of {opponent_handling}, and luck factor of {opponent_luck}!')

# Main race loop
choice = ''

while True:
    if choice == 'e':
        print(f"You decided to forfeit the race, and the {opponent_car} zooms past, claiming victory.")
        break

    choice = input("Do you (e)xit or (r)ace?: ")

    if choice == 'r':
        # Your car's turn to race
        your_race_boost = random.randint(0, your_max_boost)
        final_your_speed = your_speed + your_race_boost + (your_handling * 2) + your_luck  # Adding handling and luck factors

        print(f'You push your car to its limits, reaching {final_your_speed} mph with handling and luck boosting your performance!')

        # Opponent's turn to race
        opponent_race_boost = random.randint(0, your_max_boost)
        final_opponent_speed = opponent_speed + opponent_race_boost + (opponent_handling * 2) + opponent_luck

        print(f'The {opponent_car} hits a speed of {final_opponent_speed} mph with its handling and luck factored in!')

        # Determine who wins
        if final_your_speed > final_opponent_speed:
            print(f'You speed past the {opponent_car} and win the race!\n')
            break
        elif final_your_speed < final_opponent_speed:
            print(f'The {opponent_car} races ahead, leaving you behind. You lost the race.\n')
            break
        else:
            print(f"It's a tie! Both you and the {opponent_car} finished at the same speed!\n")
            break

print("Hope you had fun racing!")
