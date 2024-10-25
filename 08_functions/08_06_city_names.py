

def city_country(city, country):
    """Return a string like 'Toronto, Canada'."""
    return f"{city.title()}, {country.title()}"

city = city_country('toronto', 'canada')
print(city)

city = city_country('berlin', 'germany')
print(city)

city = city_country('rome', 'italy')
print(city)