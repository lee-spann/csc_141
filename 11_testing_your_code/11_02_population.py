



# 11-2 Population

def city_country_population(city, country, population=None):
    """Return a string in the form of 'City, Country – population xxx'."""
    if population:
        return f"{city.title()}, {country.title()} – population {population}"
    else:
        return f"{city.title()}, {country.title()}"

# Example usage
print(city_country_population("taranto", "canada", 91000))  # With population
print(city_country_population("taranto", "canada"))  # Without population

