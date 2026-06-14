### m07/guess6.py
import random

def main():
    secret = random.randint(1, 100)
    # print(f"The secret number is {secret}")

    while True:   # our game loop
        # Grab the player's guess
        while True:
            try:
                guess = int(input('Please input your guess: '))
                break
            except ValueError:
                print('Guesses must be an integer. Try again...')

        # Check guess against the secret
        if guess == secret:
            print('Exactly! You win!')
            break
        elif guess < secret:
            print('Too small!')
        else:
            print('Too big!')

if __name__ == '__main__':
    main()