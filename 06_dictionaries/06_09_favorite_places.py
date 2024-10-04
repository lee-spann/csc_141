

favorite_places = {
    'lee': ['bahamas', 'japan', 'florida'],
    'rodnique': ['hawaii', 'new york'],
    'lawrence': ['new jersey', 'pennsylvania', 'disney world']
    }

for name, places in favorite_places.items():
    print(f"\n{name.title()} likes the following places:")
    for place in places:
        print(f"- {place.title()}")