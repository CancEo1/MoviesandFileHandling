# This program reads a file containing movie titles and their release years
# When finding a file you need to use the full path to the file so that the program knows
# EXACTLY where to find the file.
FILENAME = "B:\Assignments for school\AdvancedPythonCSC2017\Files\Project1\examples\movies.txt"

# using a with statement will close the file automatically
def write_movies(movies):
    with open(FILENAME, "w") as file:
        for movie in movies:
            file.write(f"{movie}\n")

# This function reads the movies from the file and returns a list of movie titles
def read_movies():
    movies = []
    with open(FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            movies.append(line)
    return movies

def list_movies(movies):
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie}")
    print()

def add_movie(movies):
    movie = input("Enter the movie title: ")
    movies.append(movie)
    write_movies(movies)
    print(f"{movie} was added.\n")

def delete_movie(movies):
    index = int(input("Number: "))
    if index < 1 or index > len(movies):
        print("Invalid movie number.\n")
    else:
        movie = movies.pop(index - 1)
        write_movies(movies)
        print(f"{movie} was deleted.\n")

def display_menu():
    print("The Movie List program")
    print()
    print("Command Menu")
    print("list - List all movies")
    print("add - Add a movie")
    print("delete - Delete a movie")
    print("exit - Exit program")
    print()

def main():
    display_menu()
    movies = read_movies()
    while True:
        command = input("Command: ")
        if command.lower() == "list":
            list_movies(movies)
        elif command.lower() == "add":
            add_movie(movies)
        elif command.lower() == "delete":
            delete_movie(movies)
        elif command.lower() == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid command. Please try again.\n")

if __name__ == "__main__":
    main()
