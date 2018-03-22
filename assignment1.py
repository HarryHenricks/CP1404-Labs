"""
Harry Henricks, 17/03/2018, This console-based python program is designed for the user to be able to keep track of
movies they have watched or wish to watch via user input, https://github.com/CP1404-2018-1/a1-HarryHenricks
References:
Baetge, R. (2016). Reading List (Version 1.0). JCU Cairns.
Punch, W., & Enbody, R. The practice of computing using Python.
"""
import csv
"""
Main user interface, repeats until user chooses to quit
"""


def main():
    print("Movies To Watch 1.0 - by Harry Henricks")
    print("""Please choose either:
M - Movie list program
T - Tv list program """)
    choice = ''
    x = True  # instead of using while True and using break to exit the loop (more chance of error)
    try:
        while x:
            choice = input(">>> ").upper()
            if choice == 'M':
                choice = 'movie'
                x = False
            elif choice == 'T':
                choice = 'tv show'
                x = False
            else:
                print("Please enter a valid input")
                choice = input(">>> ").upper()
    except ValueError:
        print("Error, incorrect menu choice")
    movie_list = load_movies(choice)
    show_menu(choice)
    user_input = input(">>> ").upper()
    while user_input != 'Q':
        if user_input == 'L':
            list_movies(movie_list, 'List', choice)
            show_menu(choice)
        elif user_input == 'A':
            movie_list = add_movie(movie_list, choice)  # will update movie list when a new one is added
            show_menu(choice)
        elif user_input == 'W':
            watch_movie(movie_list, choice)
            show_menu(choice)
        elif user_input == 'R':
            remove_movie(movie_list, choice)
            show_menu(choice)
        else:
            print("Please enter a valid menu choice")
            show_menu(choice)
        user_input = input(">>> ").upper()
    confirmation = input("Please enter: 'Q' to save and quit, 'U' to quit without saving or 'R' to restart ").upper()
    if confirmation == 'N':
        main()
    elif confirmation == 'U':
        print("Goodbye, no movies saved to {}s.csv".format(choice))

    elif confirmation == 'Q':
        save_movies(movie_list, choice)
        print("{} movies saved to {}s.csv".format(len(movie_list), choice))
        print("Goodbye! See you next time")


"""
Displays menu
"""


def show_menu(choice):
    print("""{} Menu:
L - List {}s
A - Add new {}
W - Watch a {}
Q - Quit""".format(choice.capitalize(), choice, choice, choice))


"""
    function load_movies()
        open file movies.csv for reading
        movies = empty list
        movie_reader uses csv reader to read file
        for each line in file
            add line to end of movie_list
        close file
        print length of movie_list (movies loaded)       
        return movie_list
"""
"""
Loads movies into a list of lists
"""


def load_movies(choice):
    movie_file = ''
    if choice == 'movie':
        movie_file = open("movies.csv", "r")  # open movie file and initialise variables
    elif choice == 'tv show':
        movie_file = open("shows.csv", "r")
    else:
        print("Error in load_ movies function")
    movie_list = []
    movie_reader = csv.reader(movie_file)
    sorted_list = sorted(movie_reader, key=lambda row: int(row[1]))
    for line in sorted_list:  # creates movie list of lists
        movie_list.append(line)
    movie_file.close()
    print("{} {}s loaded".format(len(movie_list), choice))
    return movie_list


"""
Displays movies formatted and returns number movies left to watch
"""


def list_movies(movie_list, user_input, choice):
    to_watch = 0
    already_watched = 0
    display_list = []
    for num, movie in enumerate(movie_list):
        watched = ''  # where * indicates needs to be watched ie. not watched
        if movie[3] == 'y':
            watched = ' '
            already_watched += 1
        elif movie[3] == 'n':
            watched = '*'  # enters a space to keep movie list lined up with the unwatched
            to_watch += 1
        else:
            print("Error occurred in file, missing 'n' or 'y' from end of line {} in file {}s.csv".format(num, choice))
        temp_list = [watched, movie[0], movie[1], movie[2]]
        display_list.append(temp_list)
    if to_watch != 0 or user_input == 'List':  # don't want to display when no more movies if calling this fn from 'W'
        for num, movie in enumerate(display_list):
            print("{:3}. {} {:50} - {:4} ({})".format(num, movie[0], movie[1], movie[2], movie[3]))
        print("{} {}s watched, {} {}s still to watch".format(already_watched, choice, to_watch, choice))
    return to_watch


"""
Function to add and save a movie into the movie list of lists
"""


def add_movie(movie_list, choice):
    print("Enter Q at any time to quit back to the main menu")
    title = input("What is the title of the {}: ".format(choice))
    if title.upper() == 'Q':
        return movie_list
    while title == '' or title == ' ':  # only need to make sure not blank, titles are allowed numbers and special chars
        print("Error, title cannot be blank")
        title = input("What is the title of the {}: ".format(choice))
        if title.upper() == 'Qa':
            return movie_list
    category = input("What is the category of the {}: ".format(choice))
    if category.upper() == 'Q':
        return movie_list
    while category == '' or category == ' ':
        print("Error, category cannot be blank")
        category = input("What is the category of the {}: ".format(choice))
        if category.upper() == 'Q':
            return movie_list
    year = ''
    x = True
    while x:
        try:
            year = int(input("What year was the {} made: ".format(choice)))
            if year <= 0:
                print("Error, year must be greater than zero")
            elif year > 2018:
                print("Hello time traveller")
            elif 0 < year <= 2018:
                x = False
            else:
                print("Error, please enter a valid year")
        except ValueError:
            print("Did you want to quit?")
            quit_prompt = input("Y or N").upper()
            if quit_prompt == 'Y':
                return  # return nothing and send user back to menu
    print("{} ({} from {}) added to {} list".format(title, category, year, choice))
    movie_list.append([title, year, category, "n"])
    return movie_list  # return new movie as a list so user can enter multiple new movies in a session


"""
Function to overwrite csv file with movie_list
"""


def save_movies(movie_list, choice):
    if choice == 'movie':
        with open("movies.csv", 'w', newline='') as movie_file:
            csv.writer(movie_file).writerows(movie_list)  # overwrites file with updated list
    elif choice == 'tv show':
        with open("shows.csv", 'w', newline='') as show_file:
            csv.writer(show_file).writerows(movie_list)
    else:
        print("Error in save_movies function")
    """
    function watch_movie(movie_list):
        if function list_movies(movie_list, 'Watch') returns 0
            Display "No more movies to watch"
            return movie_list
        otherwise Display "Enter number to be mark as watched"
        try while True
                user_input = integer input
                if user_input less than 0
                    display "Error, number must be between 0 and length of movie_list"
                    break
                otherwise selected_movie = users input choice
                    if third row in selected_movie == 'n'
                        change that value to 'y'
                        update selected_movie
                        display "Movie from year marked watched" 
                        if function list_movies(movie_list, 'Watch') returns 0
                            display "No more movies to watch"
                        break out of while loop
                    else if third row in selected_movie == 'y':
                        Display "You have already watched that movie"
                        break out of while loop
        except Error
            Display "Error invalid input, please enter a number"
        open file movies.csv for overwriting
        overwrite file with updated list
    """


"""
Function to edit the y or n in csv file to indicate watched vs unwatched
"""


def watch_movie(movie_list, choice):
    if list_movies(movie_list, 'Watch', choice) == 0:
        print("No more {}s to watch".format(choice))
        return movie_list
    else:
        print("Enter number to be mark as watched")
    x = True
    try:
        while x:
            user_input = int(input(">>> "))
            if user_input < 0:
                print("Error, number must be between 0 and {}".format(len(movie_list)))
                x = False
            else:
                if user_input >= len(movie_list):  # since indexing begins at 0 and len begins counting from 1
                    print("Error, enter an integer between 0 and {}".format(len(movie_list)-1))
                    x = False
                selected_movie = movie_list[user_input]
                if selected_movie[3] == 'n':
                    selected_movie[3] = 'y'  # update movie as watched
                    movie_list[user_input] = selected_movie
                    print("{} from {} marked watched".format(selected_movie[0], selected_movie[1]))
                    if list_movies(movie_list, 'Watch', choice) == 0:
                        print("No more {}s to watch".format(choice))
                    x = False
                elif selected_movie[3] == 'y':
                    print("You have already watched {}".format(selected_movie[0]))
                    x = False
    except ValueError:
        print("Error invalid input, please enter an integer between 0 and {}".format(len(movie_list)-1))
    if choice == 'movie':
        with open("movies.csv", 'w', newline='') as movie_file:
            csv.writer(movie_file).writerows(movie_list)  # overwrites file with updated list
    elif choice == 'tv show':
        with open("show.csv", 'w', newline='') as movie_file:
            csv.writer(movie_file).writerows(movie_list)
    else:
        print("Error in watch_movie function")


def remove_movie(movie_list, choice):

    # TODO:





if __name__ == '__main__':
    main()
