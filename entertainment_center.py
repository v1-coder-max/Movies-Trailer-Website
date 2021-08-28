import fresh_tomatoes

import media

toy_story = media.Movie("Toy Story","Story is about A small child and his toy","http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=rNk1Wi8SvNc")

#print(toy_story.title)

avatar = media.Movie("Avater","A marine on a alien planet","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")

money_heist = media.Movie("Money Heist","Story is About a Historical Heist","https://upload.wikimedia.org/wikipedia/commons/f/f7/Casadepapelwordmark.png","https://www.youtube.com/watch?v=htqXL94Rza4")

dark = media.Movie("Dark","Story is about Time Travel","	https://upload.wikimedia.org/wikipedia/commons/c/cb/Dark_logo.png","https://www.youtube.com/watch?v=rrwycJ08PSA")

mirzapur = media.Movie("Mirzapur","Story is about Gangster","https://upload.wikimedia.org/wikipedia/en/3/3c/Poster_of_Mirzapur_2018.jpg","https://www.youtube.com/watch?v=ZNeGF-PvRHY")

avengers = media.Movie("Avengers","Story is about Saving the world","	https://upload.wikimedia.org/wikipedia/en/8/8a/The_Avengers_%282012_film%29_poster.jpg","https://www.youtube.com/watch?v=TcMBFSGVi1c")

#print(avatar.storyline)

#avatar.show_trailer()
movies = [toy_story,avatar,money_heist,dark,mirzapur,avengers]
fresh_tomatoes.open_movies_page(movies)
