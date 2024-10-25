

def make_shirt(size, message):
    """Summarize the shirt that's going to be made."""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')

make_shirt('large', 'This is a large t shirt')
make_shirt(message="This is a medium t shirt.", size='medium')