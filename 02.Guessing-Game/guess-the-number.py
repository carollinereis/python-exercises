import random

def guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print('====== Welcome to the guessing game!====== ')
    print('I have selected a number between 1 and 100.')
    print('Can you guess what it is?')

    while True:
        attempts += 1

        user_guess = input('What is your guess? ')
        
        try:							
	        guessed_num = int(user_guess)
        except ValueError:
            print('Oops, that is not a valid number! Please try again.')
            continue

        if guessed_num < 1 or guessed_num > 100:
            print('Remember, the number must be between 1 and 100. Try again!')
            continue

        if guessed_num == secret_number:
            print(f'Congratulations! You guessed the number {secret_number} in {attempts} attempts!')
            break
        elif guessed_num < secret_number:
             print('Too low! Try again.')
        else:
             print('Too high! Try again.')

if __name__ == '__main__':
    guessing_game()