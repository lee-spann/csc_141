


from city_functions import city_country_population


def test_city_country():
    result = city_country_population("taranto", "canada")
    assert result == "Taranto, Canada"  # Check if it works without population

def test_city_country_population():
    result = city_country_population("taranto", "canada", 91000)
    assert result == "Taranto, Canada – population 91000"  # Check if it works with population
