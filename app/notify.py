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