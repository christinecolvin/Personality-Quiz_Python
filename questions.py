"""
All types of questions asked by the program to the user with the possible valid responses.
Author: Christine Colvin
"""

import question_types


def question_1():
    user_input = question_types.ask_true_false_question("True or False: I make my bed in the morning. ")
    if user_input:  # Very productive start! I congratulate you.
        return 5
    else:  # GET IT TOGETHER
        return -10


def question_2():
    user_input = question_types.ask_yes_no_question("Do you consider yourself a dare-devil? ")
    if user_input:  # Do a flip...right now, I dare you
        return 5
    else:  # LOSER
        return -5


def question_3():
    user_input = question_types.ask_yes_no_question("Do you truly believe humans have free will? ")
    if user_input:  # 01110010 01110101 01101110 00100000 01110111 01101000 01101001 01101100 01100101
        # 00100000 01111001 01101111 01110101 00100000 01100011 01100001 01101110
        return -10
    else:  # Okay :)
        return 5


def question_4():
    user_input = question_types.ask_multiple_choice_question("Out of the 4 options, which do you find most enjoyable? ",
                                                             ["Reading books", "Coding",
                                                              "Scrap-booking", "Playing games"])
    user_input.lower()
    if user_input == "a":
        return 5  # you're lying to yourself but okay.
    elif user_input == "b":
        return -15  # I BEG of you to get a real hobby that is actually fun. TURN ON A PLAYSTATION.
    elif user_input == "c":
        return -5  # This is for old people.
    elif user_input == "d":
        return 10  # I am biased because I play them competitively.


def question_5():
    user_input = question_types.ask_multiple_choice_question("Are you enjoying playing this quiz together? :) ",
                                                             ["Yes", "No",
                                                              "Who are you?"])
    if user_input == "a":
        return 5
    elif user_input == "b":
        return -5
    elif user_input == "c":
        return -10  # Python, of course :)


def question_6():
    user_input = question_types.ask_multiple_choice_question("How often do you drink water?",
                                                             ["I always make sure to fill my water bottle.",
                                                              "I do not own a water bottle.",
                                                              "I only drink water."])
    user_input.lower()
    if user_input == "a":
        return 5  # hydration is important, i do not wish death upon you!
    elif user_input == "b":
        return -10  # you are a dry, dry, dirty cheese
    elif user_input == "c":
        return 10  # I wish I could be as strong as you.


def question_7():
    user_input = question_types.ask_numerical_question("How old are you? ", 1, 99)
    if user_input < 18:  # NOT ENOUGH TIME TO AGE. GROW UP
        return -10
    elif 18 <= user_input <= 45:
        return 5
    else:  # I prefer older men... i mean..older cheeses
        return 15


def question_8():
    user_input = question_types.ask_yes_no_question(f'Are you a "Hello Kitty" fan? ')
    if user_input:  # LOL LOL LOL
        return 10
    else:  # LOSER
        return -5


def question_9():
    user_input = question_types.ask_numerical_question("How often do you think of *finally* breaking the 4th wall? ", 1,
                                                       99)
    if user_input <= 50:  # You can not win here.
        return -10
    elif user_input > 50:  # You have no power.
        return -15


def question_10():
    user_input = question_types.ask_true_false_question("True or False: I am fully aware. ")
    if user_input:  # Are you?
        return -5
    else:  # Are you even fully aware of your lack of awareness?
        return -15
