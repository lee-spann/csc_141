

favorite_numbers = {'Jayden': [5, 16] , 
                'Jaymeir': [13, 14] , 
                'Ricky': [11, 12] ,
                'Kai': [15, 0] ,
                'Faith': [8, 88]}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()} likes the numbers...")
    for number in numbers:
        print(f"  {number}")