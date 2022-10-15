class Movie:

    def __init__(self, title, base_elo=1000):
        self.title = title
        self.elo = base_elo

    def set_elo(self, elo):
        self.elo = elo

    def equals(self, movie):
        return self.title == movie.title
