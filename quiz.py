"""
Registers the name of the player and tells them about the quiz they are about to take.
Author: Christine Colvin
"""

import questions
import time


def player_score(overall_score):
    if 25 <= overall_score <= 50:
        return "You are Brie! You're creamy, rich, and full of life. Often paired with grapes, crackers, wine...and maybe me :)"
    elif 25 > overall_score >= -25:
        return "You are Cheddar! A true crowd-pleaser--you are buttery & smooooth with lots of nutty notes. Kudos to you!"
    elif -25 > overall_score >= -50:
        return "You are Feta. Crumbly & Tangy, you are diverse in lots of dishes. Dishes that belong in the garbage. "
    elif -50 > overall_score >= -105:
        return "You are Blue Cheese. You are sharp, bold and often misunderstood. For a good reason, no one likes you. "


def main():
    users_name = input("Hello :) Register your name: ")
    print(f'Great! It is nice to meet you {users_name}. I hope we can become best friends.')
    print(f'I know you are curious...')
    time.sleep(1)
    print(f'...to figure out what kind of cheese you are! 10 questions will determine your fate. ')
    time.sleep(1)
    print("----------------------")

    question_1 = questions.question_1()
    question_2 = questions.question_2()
    question_3 = questions.question_3()
    question_4 = questions.question_4()
    question_5 = questions.question_5()
    question_6 = questions.question_6()
    question_7 = questions.question_7()
    question_8 = questions.question_8()
    question_9 = questions.question_9()
    question_10 = questions.question_10()

    print(f'You are all done! Give me a second to think about which cheese you really remind me of...')
    time.sleep(2)
    print("Hmm...interesting")
    time.sleep(2)
    print("------------")

    overall_score = question_1 + question_2 + question_3 + question_4 + question_5 + question_6 + question_7 + question_8 + question_9 + question_10

    print(f'Thank you for taking this quiz with me, {users_name}.\n{player_score(overall_score)}')
    print(f"Your overall score was {overall_score}! Please... stay here with me and play again. :) ")


if __name__ == '__main__':
    main()
