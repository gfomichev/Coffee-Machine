class Painting:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    def __str__(self):
        return f'"{self.title}" by {self.artist} ({self.year}) hangs in the Louvre.'


_title = input()
_artist = input()
_year = input()
mona_liza = Painting(_title, _artist, _year)

print(str(mona_liza))
