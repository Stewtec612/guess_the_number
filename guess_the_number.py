
from itertools import count
import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'  ## comments 


def configure_range():
    """ Set the high and low values for the random number plus """
    return 1, 10  #comment


def generate_secret(low, high):
    """ Generate a secret number for the user to guess """
    return random.randint(low, high)


def get_guess():
    """ get user's guess, as an integer number """
    return int(input('Guess the secret number? '))  #comments are fun


def check_guess(guess, secret):
    """ compare guess and secret, return string describing result of comparison """
    #checks to see if the guess is too high or too low or correct. 
    count = 0  #initialize counter
    if guess == secret:
        count =+ 1
        print('')
        return correct
    if guess < secret:
        count =+ 1
        return too_low
    if guess > secret:
        count =+ 1
        return too_high, count


def main():

    (low, high) = configure_range()
    secret = generate_secret(low, high)

    while True:
        guess = get_guess()
        result = check_guess(guess, secret)
        print(result)

        if result == correct:
            break

    print('Thanks for playing the game!')
    #print(f'Thanks for playing the game! Counter Result was {count} tries')



if __name__ == '__main__':
    main()
