import media
import fresh_tomatoes

# creates 6 instances of Movie Class
star_trek = media.Movie("Star Trek Beyond",
                        "The U.S.S. Enterprise crew explores the furthest reaches of uncharted space, where they encounter a new ruthless enemy, who puts them, and everything the Federation stands for, to the test.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BZDRiOGE5ZTctOWIxOS00MWQwLThlMDYtNWIwMDQwNzBjZDY1XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY500_CR0,0,337,500_AL_.jpg",
                        "https://www.youtube.com/watch?v=XRVD32rnzOw")

rogue_one = media.Movie("Rogue One",
                        "The Rebel Alliance makes a risky move to steal the plans for the Death Star, setting up the epic saga to follow.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjEwMzMxODIzOV5BMl5BanBnXkFtZTgwNzg3OTAzMDI@._V1_SY1000_SX675_AL_.jpg",
                        "https://www.youtube.com/watch?v=frdj1zb9sMY")

back_future = media.Movie("Back to the Future",
                          "Marty McFly, a 17-year-old high school student, is accidentally sent 30 years into the past in a time-traveling DeLorean invented by his close friend, the maverick scientist Doc Brown.",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BZmU0M2Y1OGUtZjIxNi00ZjBkLTg1MjgtOWIyNThiZWIwYjRiXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,643,1000_AL_.jpg",
                          "https://www.youtube.com/watch?v=qvsgGtivCgs")

jurassic_park = media.Movie("Jurassic Park",
                            "During a preview tour, a theme park suffers a major power breakdown that allows its cloned dinosaur exhibits to run amok.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMjM2MDgxMDg0Nl5BMl5BanBnXkFtZTgwNTM2OTM5NDE@._V1_.jpg",
                            "https://www.youtube.com/watch?v=lc0UehYemQA")

wall_e = media.Movie("WALL E",
                     "In the distant future, a small waste-collecting robot inadvertently embarks on a space journey that will ultimately decide the fate of mankind.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMjExMTg5OTU0NF5BMl5BanBnXkFtZTcwMjMxMzMzMw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=alIq_wG9FNk")

the_martian = media.Movie("The Martian",
                          "An astronaut becomes stranded on Mars after his team assume him dead, and must rely on his ingenuity to find a way to signal to Earth that he is alive.",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc2MTQ3MDA1Nl5BMl5BanBnXkFtZTgwODA3OTI4NjE@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                          "https://www.youtube.com/watch?v=ej3ioOneTy8")

# assign the instances into an array
movies = [star_trek, rogue_one, back_future,
          jurassic_park, wall_e, the_martian]

# call fresh_tomatoes to generate html contents
fresh_tomatoes.open_movies_page(movies)
