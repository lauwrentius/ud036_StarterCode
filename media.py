import webbrowser


class Movie():
    """This class is a movie class"""

    def __init__(self, title, storyline, poster_image_url,
                 trailer_youtube_url):
        """
        Movie Class constructor

        Parameters
        ----------
        title : string
            Movie title
        synopsis : string
            Movie storyline
        poster_image_url : string
            Movie poster web URL
        trailer_youtube_url : string
            Movie trailer youtube URL            
        """
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
