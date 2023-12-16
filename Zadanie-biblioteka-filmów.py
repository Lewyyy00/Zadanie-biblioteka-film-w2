import random

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

class Media_library:
    def __init__(self):
        self.media_list = []

    def get_media(self, media):
        self.media_list.append(media)

    def get_movies(self):
        movies = [media for media in self.media_list if isinstance(media, Movie)]
        return sorted(movies, key=lambda x: x.title)

    def get_series(self):
        series = [media for media in self.media_list if isinstance(media, Series)]
        return sorted(series, key=lambda x: x.title)
    
    def top_titles(self, n, media_type=None):
        if media_type == "movies":
            sorted_media = sorted(self.get_movies(), key=lambda x: x.views, reverse=True)
        elif media_type == "series":
            sorted_media = sorted(self.get_series(), key=lambda x: x.views, reverse=True)
        else:
            sorted_media = sorted(self.media_list, key=lambda x: x.views, reverse=True)

        return sorted_media[:n]

    def search(self, title):
        results = [media for media in self.media_list if title.lower() in media.title.lower()]
        return results
    
    def generate_views(self, n=1):
        for _ in range(n):
            random_media = random.choice(self.media_list)
            random_views = random.randint(1, 100)
            random_media.play(random_views)
    

