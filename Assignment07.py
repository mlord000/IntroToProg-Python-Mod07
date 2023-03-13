# ------------------------------------------------------------------------ #
# Title: Assignment 07
# Description: This file demonstrates examples of exception handling and
#     pickling in the python language. The examples provided here are based
#     on code reviewed in class assignments as well as information from the
#     following websites:
#
#         * regarding exception handling *
#         https://docs.python.org/3/tutorial/errors.html
#             Examples directly from the python documentation, there are
#             very detailed examples and descriptions to be found here.
#         https://www.programiz.com/python-programming/exception-handling
#             The above webpage was useful because it demonstrated examples
#             which stepped through some of the levels of exception handling.
#             For example, incorporating an "else:" code block or using the
#             "finally:" code block after a try:/exception:
#         https://www.geeksforgeeks.org/python-exception-handling/
#             The above webpage was helpful because it listed and described
#             different types of exceptions that can be used within the
#             exception block.
#
#         * regarding pickling *
#         https://www.geeksforgeeks.org/understanding-python-pickling-example/
#             I feel this is good at explaining the subject because it gives
#             a straightforward example of storing and retrieving the data.
#         https://www.digitalocean.com/community/tutorials/python-pickle-example
#             I appreciated this example because it demonstrates collecting
#             user-entered data and picking this into a file (writing of
#             pickle.dump()) as well as opening (pickle.load()) and
#             displaying the data back to the user.
#         https://wiki.python.org/moin/UsingPickle
#             From the python wiki, the most simple pickle example I have
#             come across.
#
# ChangeLog (Who,When,What):
# Matthew Lord,2023.03.09 @ 10:36PM,Created file
# Matthew Lord,2023.03.09 @ 10:55PM,Completed description of file
# Matthew Lord,2023.03.09 @ 11:59PM,Completed try/except section of the code
# Matthew Lord,2023.03.12 @ 3:47PM,Added functions to the try/except section
#     of the code and made an attempt at separating the code into three
#     section of data/processing/input-output
# Matthew Lord,2023.03.12 @ 6:42PM,Added a functional pickle example block.
#     NOTES: this section can be further refined to provide more clear or
#         direct options to the user, such as:
#             - append the saved list with the current session list
#             - clear/delete the current session/saved lists either
#               separately or as a whole (clear/delete all data)
#             - clear/delete a specific word from the current session or the
#               list of saved data
#         This would give more control to the user.
# Matthew Lord,2023.03.12 @ 7:27PM,Wrapping up this code for the assignment
#     in order to move on. Seems to run well, though could be refined and/or
#     combined I'm sure.
# Matthew Lord,2023.03.12 @ 8:02PM,Dealt with an error in the pickle section
#     of code when I file does not already exist. Using the os library and
#     importing the os.path module to use isFile()
#
# ------------------------------------------------------------------------ #


# BEGIN DATA ------------------------------------------------------------- #

import random  # include the random library
import pickle  # include the pickle library
import os.path  # include this to verify the file exists

# declare variables
user_input = str
numerator = int
menu_choice = str
session_list = []
pickle_list = []
file_name = "ListOfWords"

# END DATA --------------------------------------------------------------- #


# BEGIN PROCESSING ------------------------------------------------------- #

# functions to inform user of each section of code
def TryExceptMsg():
    # inform the user that this code will demonstrate exception handling with
    #     custom messages
    print("\n* THIS PORTION OF THE SCRIPT WILL DEMONSTRATE ERROR HANDLING USING TRY/EXCEPT:")
    return  # nothing to return

def PicklingMsg():
    # inform the user that this section of the script will demonstrate pickling
    print("\n\n* THIS PORTION OF THE SCRIPT WILL DEMONSTRATE PICKLING:")
    return  # nothing to return

# functions to inform the user of instructions for each section of code
# instructions for the first code demonstration of try/except error handling
def TryExceptInstructions():
    # inform the user of what this portion of the program will do
    print("\nWe will collect a number from you and apply it to the\n"
          + "denominator of a fraction, then return the quotient.")
    print("\nType 'exit' to move on to the pickling portion of the assignment...")
    print("\n*** (To force an exception, enter '0', a float number, or a string other than 'exit'.) ***")
    return  # nothing to return

# function to retrieve user input
def UserInput():
    # collect input from the user
    usr_input = input("\nPlease enter a number for the denominator: ")
    return usr_input  # return the user input

# function to handle the math (in this case, division)
def GetQuotient(num, den):
    # convert to integers for math operation
    num = int(num)
    den = int(den)
    q = num/den  # math for quotient
    return q  # return the quotient

# create a random numerator
def GetNumerator():
    # assign a random number (1-9) to the numerator
    num = random.randrange(1, 9)
    return num  # return the numerator

# function to display the fraction
def ShowFraction(num, den):
    # inform the user of the fraction
    print("The fraction we have created is: ", str(num), "/", str(den))
    return  # nothing to return

# display a menu to the user for the pickling section of code
def MenuDisplay():
    print("""
    Menu of Options
    1) Add a word to the current session list
    2) Display the current session list
    3) Overwrite the saved data with the current session list
    4) Display the saved data using pickle
    5) Exit the program
    """)
    return  # nothing to return

# get a menu choice from the user
def MenuSelection():
    menu_select = input("Which option would you like to perform? [1 to 5] - ")
    print()  # adding a new line for looks
    return menu_select

# function to verify menu choice in pickle section of code
def MenuVerify(menu_selection):
    if menu_selection not in ['1', '2', '3', '4', '5']:
        print("*** PLEASE ENTER ONLY AN OPTION 1 - 5! ***")
    return  # nothing to return

# END PROCESSING --------------------------------------------------------- #


# BEGIN INPUT/OUTPUT ----------------------------------------------------- #

# CODE THAT PROVIDES A BASIC DEMONSTRATION OF EXCEPTION HANDLING
# inform user what this portion of the code is for
# this case: try/except error handling
TryExceptMsg()

# a loop for the try/except block
while True:
    # begin try/exception block
    try:
        # provide instructions to user
        TryExceptInstructions()
        # get user input and assign it to a variable for this iteration of
        #     the while loop
        user_input = UserInput()
        # check user_input for 'exit'
        if user_input.lower() == "exit":
            break  # move to the next section of code (re: pickling)
        # get a random numerator and assign to a variable for this iteration
        #     of the while loop
        numerator = GetNumerator()
        # display the fraction to the user
        ShowFraction(numerator, user_input)
        # display the quotient to the user
        print("The quotient is: ", GetQuotient(numerator, user_input))

    # provide exception handling if a user enters "0" for the denominator
    except ZeroDivisionError:
        # feedback to the user before continuing through the while loop
        print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -" +
              "\nERROR: we can not divide by 0..." +
              "\nPlease retry and enter a number greater than 0." +
              "\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

    # provide exception handling if a user enters a string or float for the denominator
    except ValueError:
        # feedback to the user before continuing through the while loop
        print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -" +
              "\nERROR: please enter a whole number for the denominator." +
              "\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")


# CODE THAT PROVIDES A BASIC DEMONSTRATION OF PICKLING
# inform user what this portion of the code is for
# this case: pickling example
PicklingMsg()

# loop for the pickling block of code
while (True):
    # display the menu
    MenuDisplay()
    # get a menu choice from the user
    menu_choice = MenuSelection()
    # check menu_choice/user input
    MenuVerify(menu_choice)

    # Add a new word/string to the list
    if (menu_choice.strip() == '1'):
        # prompt user for a task to add to the list/table
        user_word = input("Enter a word: ")
        # add the word to a list
        session_list.append(user_word)
        # inform the user what action has taken place
        print("We have added the word '" + user_word + "' to the current session list.")
        continue  # continue to the while/menu loop

    elif (menu_choice.strip() == '2'):
        # print the current list of words
        print("The current list of words in this session is:")
        print(session_list)

    elif (menu_choice.strip() == '3'):
        # verify the user wants to overwrite
        user_input = input("Are you sure you want to overwrite the saved data? (Y or N): ")
        # check value of user input
        if user_input.lower() == "y":
            # assign the current list to a list to be saved
            pickle_list = session_list
            # save the list as a binary file using pickle
            pickle.dump(pickle_list, open(file_name, "wb"))
            # inform the user of what action has taken place
            print("You have overwritten the saved data with the current list of words.")
        elif user_input.lower() == "n":
            # inform the user
            print("You have chosen NOT to overwrite the saved data.")
        else:
            print("\nPlease use only 'Y' or 'N'")
            print("Select a menu option:")
        continue  # continue to the while/menu loop

    elif (menu_choice.strip() == '4'):
        if os.path.isfile(file_name):
            # open and load the saved list using pickle
            pickle_list = pickle.load(open(file_name, "rb"))
        else:
            # inform the user that the file doesn't exist
            print("There is no data file saved... we will create one.")
            # create the file
            pickle.dump(pickle_list, open(file_name, "wb"))
            # inform the user that the file has been created
            print("The file has been created. It is currently empty.")
        # display the list to the user
        print("The saved list of data is: ")
        print(pickle_list)

    elif (menu_choice.strip() == '5'):
        # verify the user would like to exit the program
        user_input = input("Would you like to exit the program? (Y or N): ")
        # check value of user input
        if user_input.lower() == "y":
            # inform user they have exited the program
            print("You have exited the program.")
            break  # and Exit the program
        elif user_input.lower() == "n":
            # inform the user they have chosen NOT to exit the program
            print("You have chosen NOT to exit the program.")
            continue  # continue to the while/menu loop
        else:
            print("\nPlease use only 'Y' or 'N'")
            print("Select a menu option:")
            continue  # continue to the while/menu loop

# END INPUT/OUTPUT --------------------------------------------------- #
