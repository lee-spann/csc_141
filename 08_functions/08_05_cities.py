


def describe_city(city, country='toronto'):
    """Describe a city."""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('canada')
describe_city('tokyo', 'japan')
describe_city('montreal')