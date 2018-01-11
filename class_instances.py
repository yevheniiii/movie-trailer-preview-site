# -*- coding: utf-8 -*-

import index
import movie_class

# Create instances of the Movie class to keep information of the most expected movies in 2018

avengers_infinity_war = movie_class.Movie("Avengers: Infinity War",
                                          "The Avengers and their allies must be "
                                          "willing to sacrifice all in an attempt "
                                          "to defeat the powerful Thanos before his "
                                          "blitz of devastation and ruin puts an "
                                          "end to the universe.",
                                          "https://upload.wikimedia.org/wikipedia/en/9/90/Avengers_Infinity_War.jpg",
                                          "https://youtu.be/6ZfuNTqbHE8")

jurassic_world_fallen_kingdom = movie_class.Movie("Jurassic World: Fallen Kingdom",
                                                  "When the island's dormant volcan"
                                                  "o begins roaring to life, Owen "
                                                  "and Claire mount a campaign to "
                                                  "rescue the remaining dinosaurs f"
                                                  "rom this extinction-level event.",
                                                  "https://upload.wikimedia.org/wikipedia/en/c/c6/Jurassic_World_Fallen_Kingdom.png",
                                                  "https://youtu.be/vn9mMeWcgoM")

black_panther = movie_class.Movie("Black Panther",
                                  "T'Challa, after the death of his father, the Kin"
                                  "g of Wakanda, returns home to the isolated, tech"
                                  "nologically advanced African nation to succeed to"
                                  " the throne and take his rightful place as king.",
                                  "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg",
                                  "https://youtu.be/JBiZX_ceqO0")

star_wars_han_solo = movie_class.Movie("Solo: A Star Wars Story",
                                       "Han Solo and Chewbacca's adventures before "
                                       "joining the Rebellion, including their early"
                                       " encounters with Lando Calrissian.",
                                       "https://upload.wikimedia.org/wikipedia/commons/4/46/Solo-a-star-wars-story-tall-A.png",
                                       "https://youtu.be/leqzA79H8OM")

the_predator = movie_class.Movie("The Predator",
                                 "A re-make of the 1987 sci-fi film 'Predator'",
                                 "https://upload.wikimedia.org/wikipedia/en/e/e9/The_Predator_promotional_poster.jpg",
                                 "https://www.youtube.com/watch?v=egsgpDg-XKg")

aquaman = movie_class.Movie("Aquaman",
                            "Arthur Curry learns that he is the heir to the underwa"
                            "ter kingdom of Atlantis, and must step forward to lead "
                            "his people and to be a hero to the world.",
                            "https://upload.wikimedia.org/wikipedia/en/b/ba/Aquaman_movie_logo.jpg",
                            "https://youtu.be/4LIaodz21WY")

tomb_raider = movie_class.Movie("Tomb Raider",
                                "Lara Croft, the fiercely independent daughter of a "
                                "missing adventurer, must push herself beyond her "
                                "limits when she finds herself on the island where "
                                "her father disappeared.",
                                "https://upload.wikimedia.org/wikipedia/en/b/bd/Tomb_Raider_%282018_film%29.png",
                                "https://youtu.be/8ndhidEmUbI")

deadpool_2 = movie_class.Movie("Deadpool 2",
                               "After surviving a near fatal bovine attack, Wade "
                               "Wilson (Ryan Reynolds) struggles to fulfill his drea"
                               "m of becoming Mayberry’s hottest bartender while"
                               " also learning to cope with his lost sense of taste.",
                               "https://upload.wikimedia.org/wikipedia/en/c/cf/Deadpool_2_poster.jpg",
                               "https://youtu.be/8-Cjsnq8kVU")

# Add the instances to a list
movies = [
    avengers_infinity_war,
    jurassic_world_fallen_kingdom,
    black_panther,
    star_wars_han_solo,
    the_predator, aquaman,
    tomb_raider,
    deadpool_2
]

# Generate a web page that displays the movies in the list
index.open_movies_page(movies)
