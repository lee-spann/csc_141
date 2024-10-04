

cities = {
    'tokyo': {
        'country': 'japan',
        'population': 13_960_000,
        'nearby mountains': 'fuji',
    },
    'zurich': {
        'country': 'switzerland',
        'population': 428_737,
        'nearby mountains': 'alps',
    },
    'nairobi': {
        'country': 'kenya',
        'population': 4_397_073,
        'nearby mountains': 'mount kenya',
    }
}


for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    mountains = city_info['nearby mountains'].title()

    print(f"\n{city.title()} is in {country}.")
    print(f"  It has a population of about {population}.")
    print(f"  The {mountains} mounats are nearby.")