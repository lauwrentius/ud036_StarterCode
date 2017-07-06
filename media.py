import webbrowser


class Movie():
    """This class is a movie class"""

    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
