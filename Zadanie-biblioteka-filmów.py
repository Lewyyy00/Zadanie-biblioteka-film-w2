class Type_of_media:
    def __init__(self, title, year, genre, views=0):
        self.title = title
        self.year = year
        self.genre = genre
        self.views = views

    def play(self, views=1):
        self.views += views


class Movie(Type_of_media):
    def __str__(self):
        return f"{self.title} ({self.year})"


class Series(Type_of_media):
    def __init__(self, title, year, genre, season, episode, views=0):
        super().__init__(title, year, genre, views)
        self.season = season
        self.episode = episode

    def __str__(self):
        season_str = f"S{self.season:02d}"
        episode_str = f"E{self.episode:02d}"
        return f"{self.title} {season_str}{episode_str} ({self.year})"

