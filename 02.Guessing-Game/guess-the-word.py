import random
import os

def guessing_word():
    word_list = ['thought', 'beaver', 'ranch', 'wool', 'cherry', 'pen', 'sibling', 'aunt', 'picture', 'fork']
    random_words = random.choice(word_list)
    attempts = 0
    right_letters = []
    missed_letters = []
    
    print('\n'+ '='*5 + ' Welcome to the Hangman game! ' + '='*5)

    while True:
        user_guess = input('\nEnter a letter: ').strip().lower()

        if not user_guess or not user_guess.isalpha() or len(user_guess) > 1:
            print('Please enter a single letter!')
            continue

        attempts += 1

        if user_guess in random_words:
            if user_guess not in right_letters:
                right_letters.append(user_guess)
        else:
            if user_guess not in missed_letters:
                missed_letters.append(user_guess)

        won = True
        print('Word: ', end=' ')
        for letter in random_words:
            if letter in right_letters:
                    print(letter, end=' ')
            else: 
                print('*', end=' ')
                won = False
         
        print()
        print(f'Wrong guesses: {missed_letters}')

        if won:
            os.system('clear')
            print(f'\nCONGRATS! You got it!')
            print(f'The word was: {random_words}')
            print(f'Total attempts: {attempts}')
            break

if __name__ == '__main__':
    guessing_word()