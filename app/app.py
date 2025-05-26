import random
import notify

word_list = [
    'sword',
    'chaos',
    'delay',
    'lunch',
    'truck',
    'clear',
    'woman',
    'apple',
    'wrist',
    'mouth',
    'stage',
    'dance',
    'light',
    'sugar',
    'march',
    'chair'
]

def get_word_from_list():
    return random.choice(word_list)


def ask_for_guess():
    try:
        guess = input('Guess the word: ')
        return guess
    except (EOFError, KeyboardInterrupt):
        print('\n Bye!')
        exit()


def ask_to_try_again():
    try:
        answer = input('Would you like to try again? (yes/no): ')
        return True if answer.lower() == 'yes' else False
    except (EOFError, KeyboardInterrupt):
        print('\n Bye!')
        exit()


def restart_game():
    print('\n')
    print('*' * 20)
    print('Restarting game...')
    print('*' * 20)
    print('\n')


def word_raider():
    word = get_word_from_list().lower()
    max_guesses = 5
    attempts = 0

    while attempts < max_guesses:
        print(f'Attempt {attempts + 1} of {max_guesses}')

        guess = ask_for_guess().lower()

        if guess == word:
            print('You won!')
            break
        else:
            print('Incorrect!')
            report_match_attempter(letter_match_checker(word, guess))
            print('\n')
            attempts += 1

    if attempts == max_guesses:
        print(f'You lost! You did not guess the correct word. The word was {word}. Try again!')

    return False if attempts == max_guesses else True


def report_match_attempter(matches):
    if len(matches['correct']):
        print(f'Correct letters in correct positions: {matches['correct']}')

    if len(matches['correct_but_wrong_position']):
        print(f'Correct letters in wrong positions: {matches["correct_but_wrong_position"]}')


def letter_match_checker(word, guess):
    correct = []
    correct_but_wrong_position = []
    for index, letter in enumerate(word):
        for guess_index, letter_guess in enumerate(guess):
            if letter == letter_guess and index == guess_index:
                correct.append(letter)
            elif letter == letter_guess and index != guess_index:
                correct_but_wrong_position.append(letter)

    return {'correct': correct, 'correct_but_wrong_position': correct_but_wrong_position}

def main():
    notify.print_instructions()

    game_counter = 0
    won_counter = 0
    lost_counter = 0
    in_game = True

    while in_game:
        game_counter += 1
        won = word_raider()
        if won:
            won_counter += 1
        else:
            lost_counter += 1

        play_again = ask_to_try_again()

        if play_again:
            restart_game()
        else:
            print('Thanks for playing!')
            in_game = False

    notify.print_results(game_counter, won_counter, lost_counter)