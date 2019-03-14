"""
Importing entertainment_center_manual
and entertainment_center_input_file modules
"""
import entertainment_center_manual
import entertainment_center_input_file_reader


def input_type_choice_classifier():

    # Asking user for the method they want to follow
    # Enter the movie details : Manually or to read Input from a file
    # Checking for only two provided correct inputs
    while True:

        #  Avoiding case sensitive exceptions
        print("Please select the method of entering the movie data:")
        print("1. Enter M or m for Manually")
        print("2. Enter I or i for reading from an input file\n")
        input_type_choice = input().lower()
        if input_type_choice == 'm':

            # Calling movie_object_creator() for manual entry
            entertainment_center_manual.movie_object_creator()
            break

        elif input_type_choice == 'i':

            # Calling movie_object_creator() to read a file
            entertainment_center_input_file_reader.input_movies_file_reader()
            break

        else:
            print("You seem to have entered a wrong option. Please try again.")

if __name__ == "__main__":
    input_type_choice_classifier()
