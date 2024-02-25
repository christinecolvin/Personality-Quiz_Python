"""
Checks to validate the user's response to every question
Example: 'Apple' is not a valid response to a Yes or No question.
Author: Christine Colvin
"""


def ask_true_false_question(question):
    """
    Function that defines the true or false questions asked by the program to the user and depends on their answer to
    return a boolean tru or false, making sure to validate the input.
    """
    user_input = input(question).lower()
    valid_list = ['true', 'false', 't', 'f']
    while user_input not in valid_list:
        user_input = input("Please, enter a valid response (True or False.) ").lower()

    if user_input in ['true', 't']:
        return True
    if user_input in ['false', 'f']:
        return False


def ask_yes_no_question(question):
    """
    Function that defines the yes or no questions asked by the program to the user and depends on their answer to
    return a boolean true or false, making sure to valid the input.
    """
    user_input = input(question).lower()
    valid_list = ['yes', 'no', 'y', 'n']
    while user_input not in valid_list:
        user_input = input("Please, enter a valid response (Yes or No.) ").lower()

    if user_input in ['yes', 'y']:
        return True
    if user_input in ['no', 'n']:
        return False


def ask_multiple_choice_question(question, options):
    """
    Function that defines the multiple choice questions asked by the program to the user and depends on their answer
    within the given options, checks its validation using a for and while loop.
    """
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
    print(question)

    alphabet_letter = 0
    for option in options:
        print(f'{alphabet_list[alphabet_letter]}. {option}')
        alphabet_letter += 1

    response = input("Select an answer!: ").lower()

    while response not in alphabet_list[0:len(options)]:
        response = input("Are you a moron? Enter a valid input: ").lower()

    return response


def is_valid_number_in_range(value, lower, upper):
    """
    Function validates the user's input, checks if it is a digit and is within range in order to be a valid input for the
    program's question.
    """
    if value.isdigit() and lower <= int(value) <= upper:
        return True
    else:
        return False


def ask_numerical_question(question, lower, upper):
    """
    Function that defines the numerical questions asked by the program to the user and checks that the user's input is
    a valid number in range and gives prompts if not valid.
    """
    user_input = input(question)

    valid_num = is_valid_number_in_range(user_input, lower, upper)

    while not valid_num:
        if user_input.isdigit():
            user_input = input("Please, enter a valid response. ")
            valid_num = is_valid_number_in_range(user_input, lower, upper)
        else:
            user_input = input("...Do not enter that into my program :(. Choose a number in range. ")
            valid_num = is_valid_number_in_range(user_input, lower, upper)
    return int(user_input)
