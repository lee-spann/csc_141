

# This code is like 06_11, but I have added another fact about each city and printed it


cities = {
    'tokyo': {
        'country': 'japan',
        'population': 13_960_000,
        'nearby mountains': 'fuji',
        'famous landmark': 'tokyo tower',
    },
    'zurich': {
        'country': 'switzerland',
        'population': 428_737,
        'nearby mountains': 'alps',
        'famous landmark': 'grossmünster',
    },
    'nairobi': {
        'country': 'kenya',
        'population': 4_397_073,
        'nearby mountains': 'mount kenya',
        'famous landmark': 'nairobi national park',
    }
}


for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    mountains = city_info['nearby mountains'].title()
    famouslandmark = city_info['famous landmark'].title()

    print(f"\n{city.title()} is in {country}.")
    print(f"  It has a population of about {population}.")
    print(f"  The {mountains} mounats are nearby.")
    print(f" Its famous land mark is {famouslandmark}")