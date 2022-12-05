class TMDBMovie:
    def __init__(self, id, title, 
            popularity=None,
            poster_path=None,
            release_date=None,
            genre=None
        ):
        self.id = id
        self.title = title
        self.popularity = popularity
        self.poster_path = poster_path
        self.release_date = release_date
        self.genre = genre