import random

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
    guess = input('Guess the word: ')
    return guess

def ask_to_try_again():
    answer = input('Would you like to try again? (yes/no): ')
    return True if answer.lower() == 'yes' else False


def restart_game():
    print('\n')
    print('*' * 20)
    print('Restarting game...')
    print('*' * 20)
    print('\n')

def word_raider():
    word = get_word_from_list()
    max_guesses = 5
    attempts = 0

    while attempts < max_guesses:
        print(f'Attempt {attempts + 1} of {max_guesses}')

        guess = ask_for_guess()

        if guess == word:
            print('You won!')
            break
        else:
            print('Incorrect!')
            attempts += 1

    if attempts == max_guesses:
        print(f'You lost! You did not guess the correct word. The word was {word}. Try again!')

    return False if attempts == max_guesses else True


def print_instructions():
    print('Welcome to Word Raider!')
    print('A random 5 letter word will be chosen.')
    print('You have 5 attempts to guess the correct word.')
    print('Good luck!')
    print('\n')

def print_results(game_counter, won_counter, lost_counter):
    print('Game results:')
    print(f'Games played: {game_counter}')
    print(f'Games won: {won_counter}')
    print(f'Games lost: {lost_counter}')

def main():
    print_instructions()

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

    print_results(game_counter, won_counter, lost_counter)


main()