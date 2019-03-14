"""
Importing required media and fresh_tomatoes modules
"""
import media
import fresh_tomatoes


def movie_object_inputs(index):
    """
    Takes inputs for each movie object attributes from the user.

    index - Number of the movie for which attributes values are being entered.
    """
    # Taking raw input from the user for each movie's attributes
    movie_name = input("Enter the {} movie name: ".format(index))
    brief_description = input("Enter the brief description about the movie : ")
    poster_image_url = input("Enter the poster image url : ")
    youtube_trailer_url = input("Enter the YouTube trailer link : ")

    return movie_name, brief_description, poster_image_url, youtube_trailer_url


def movie_object_creator():
    """
    Creates no. of movie objects inputted by user.
    """

    # loop to check the input from user is a correct number
    while True:
        # Handling non integer input exception
        try:
            number_of_movies = int(input("Enter the number of movies : "))

            # Checking for non-zero and non-negative number
            if number_of_movies > 0:
                break
            else:
                print("You seem to have entered an incorrect no.")
                print("Please enter correct number.")
        except ValueError:
            print("The value entered is not a number. Please try again.")

    # List to store the movie objects created
    movies = []

    # Creating the number of Movie objects inputted by the user
    for index in range(number_of_movies):

        # Derefrencing returned values into seperate arguments
        movies.append(media.Movie(*movie_object_inputs(index + 1)))

    # Calling fresh_tomatoes module's open_movies_page function
    # Dynamically generates the web page for the list of movies
    fresh_tomatoes.open_movies_page(movies)

if __name__ == "__main__":
    movie_object_creator()
