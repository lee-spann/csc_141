

def make_album(artist, title):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    return album_dict

album = make_album('kendrick lamar', 'damn')
print(album)

album = make_album('drake', 'take care')
print(album)

album = make_album('kanye west', 'college dropout')
print(album)