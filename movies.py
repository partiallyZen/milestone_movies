"""
'a' to add, 'l' to see, 'f' to find, 'q' to quit

-Add movies
- See movies
- Find a movie
- Stop running

Tasks:
Show user interface and get input
Stop running when user types 'q'

"""
movies = []

"""
movie =  {
    'name':(str) 
    'director':(str)
    'year':(int)


"""


def menu():
    user_input = input("'a' to add, 'l' to see, 'f' to find, 'q' to quit: ")

    if user_input == 'q':
        print('Thanks for using Movie App!')
    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies(movies)
        elif user_input == 'f':
            find_movie()
        else:
            print('Unknown command - Please try again. ')

        user_input = input("\n'a' to add, 'l' to see, 'f' to find, 'q' to quit: ")


def add_movie():
    name = input("Enter a movie name: ")
    director = input("Enter a movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'name': name,
        'director': director,
        'year': year
    })


def show_movies(movies_list):
    for movie in movies_list:
        show_movie_details(movie)


def show_movie_details(movie):
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Release Year: {movie['year']}")


def find_movie():
    find_by = input("What property are you looking for? ")  # year, name, or director
    looking_for = input("What are you searching for? ")

    found_movies = find_by_attribute(movies, looking_for, lambda x: x[find_by])

    show_movies(found_movies)

    
def find_by_attribute(items, expected, finder):
    found = []

    for i in items:
        if finder(i) == expected:
            found.append(i)

    return found


menu()
