class Serie:
    def __init__(self, poster_link, series_title, runtime_of_series, certificate, runtime_of_episodes, genre, imdb_rating, overview, no_of_vote):
        self.poster_link = poster_link
        self.series_title = series_title
        self.runtime_of_series = runtime_of_series
        self.certificate = certificate
        self.runtime_of_episodes = int(runtime_of_episodes)
        self.genre = genre
        self.imdb_rating = imdb_rating
        self.overview = overview
        self.no_of_vote = int(no_of_vote)


    def __str__(self):
        return (f'Poster Link: {self.poster_link: <165} -- '
                f'Series Title: {self.series_title: <50} -- '
                f'Runtime of series: {self.runtime_of_series: <15} -- '
                f'Certificate: {self.certificate: <15} -- '
                f'Runtime of episodes: {self.runtime_of_episodes: <15} -- '
                f'Genre: {self.genre: <30} -- '
                f'Imdb rating: {self.imdb_rating: <15} -- '
                f'Number of votes: {self.no_of_vote: <30}')


