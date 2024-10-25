


def make_sandwich(*items):
    """Make a sandwich with the given items."""
    print("\nI'll make you a great sandwich:")
    for item in items:
        print(f"  ...adding {item} to your sandwich.")
    print("Your sandwich is ready!")

make_sandwich('ham', 'cheddar cheese', 'lettuce', 'honey mustard')
make_sandwich('turkey', 'apple slices', 'mustard')
make_sandwich('peanut butter', 'strawberry jam')