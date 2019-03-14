import media
import fresh_tomatoes


def movie_object_creator(file_data_list):
    """
    Creates no. of Movie object from the values in the passed list.

    file_data_list - list of no. of movies and movie attributes.
    """

    # loop to check the input from user is a correct number
    while True:
        # Handling non integer input exception
        try:
            number_of_movies = int(file_data_list[0])
            # Checking for non-zero and non-negative number
            if number_of_movies > 0:
                break
            else:
                print("You seem to have entered an incorrect no.")
                print("Please enter a number greater than 0.")
        except ValueError:
            print("The value entered is not a number. Please try again.")

    # List to store the movie objects created
    movies = []

    # Variable to store starting index of each object values
    # Value intialised to 1 as the 0 index points to no. of movies
    obj_index = 1
    # Creating the number of objects inputted by the user
    for index in range(number_of_movies):
        # Creating Movie objects and list of Movie objects
        list_of_each_movie_values = file_data_list[obj_index:4 + obj_index]
        movies.append(media.Movie(* list_of_each_movie_values))

        # Incrementing starting index to point o the next Movie object values
        obj_index += 4

    # Calling fresh_tomatoes module's open_movies_page function
    # Dynamically generates the web page for the list of movies
    fresh_tomatoes.open_movies_page(movies)


def input_movies_file_reader():
    """
    Reads the input file and creates Movie objects from the values
    """
    # Taking input file name or path of input file from user
    movies_input_file = input("Enter the path of the input file: ")

    # Reading the whole file and storing in a String variable input_file_data
    input_file = open(movies_input_file, 'r')
    input_file_data = input_file.read()
    input_file.close()

    # Spliting the input file data into a list of strings on basis of new line
    file_data_list = input_file_data.split('\n')

    # Calling movie object creator function
    movie_object_creator(file_data_list)

if __name__ == "__main__":
    input_movies_file_reader()
