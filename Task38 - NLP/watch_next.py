#A program to recommend the next movie to the user based on his previous watch.
import spacy

nlp = spacy.load('en_core_web_md')
movies = []         #Store the movies from the file
movies_compare_index = {}     #Store the movie and its similarity index

''' This function will read the movies from a file 'movies.txt' and store them in a list'''
def read_movies():
    global movies
    with open('movies.txt','r') as file:
        movies = file.readlines()

'''This function will loop through all the movies in the list
and for each movie it will find the similarity index by comparing the movie description with the input parameter movie description.
Finally it will store the movie name and its similarity index in a dictionary'''
def movies_compare_planethulk(planethulk_desc):
    global movies_compare_index
    nlp_hulk_desc = nlp(planethulk_desc)
    for movie in movies:
        movie_name = movie.split(":")[0]
        movie_desc = movie.split(":")[1].strip()
        print(f"{movie_name} ::: {movie_desc}")
        nlp_movie_desc = nlp(movie_desc)

        movies_compare_index[movie_name] = nlp_hulk_desc.similarity(nlp_movie_desc)

'''This is the main function that will be called from the main program.
Firstly, it will call read_movies to read all movies.
Secondly, it will compare each movie and create movies similarity index.
Lastly, it will determine the movie with the highest index and will recommend that moviee.'''
def find_matching_movie(planet_hulk_desc):
    read_movies()       
    movies_compare_planethulk(planet_hulk_desc)

    for key in movies_compare_index:
        print(f"{key},: {movies_compare_index[key]}")

    matching_movie = max(movies_compare_index, key=movies_compare_index.get)
    print(f"The recommended movie is {matching_movie}")
    return matching_movie

planet_hulk_desc = "“Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator"
find_matching_movie(planet_hulk_desc)