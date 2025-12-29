
def guessing_word():
    chosen_word = 'perfum'
    attempts = 0
    right_letters = []
    
    while True:
        user_guess = input('\nEnter a letter: ').strip().lower()

        if not user_guess or not user_guess.isalpha() or len(user_guess) > 1:
            print('Please enter letters only!')
            continue

        attempts += 1

        if user_guess in chosen_word and user_guess not in right_letters:
            right_letters.append(user_guess)
        
        won = True

        for letter in chosen_word:
            if letter in right_letters:
                    print(letter, end=' ')
            else: 
                print('*', end=' ')
                won = False
        
        print()

        if won:
            print(f'\nCONGRATS, you got it!')
            print(f'The word was: {chosen_word}')
            print(f'Total attempts: {attempts}')
            break
           
if __name__ == '__main__':
    guessing_word()