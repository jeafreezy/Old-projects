


#Written by Jolaiya Emmanuel Ayodele(jolaiyaemmanuel@gmail.com)

import sys
import random

print('********** Welcome to the guessing game********** \n '
      'Here are the rules: \n'
      '1) Start by inputting your name \n'
      '2) Provide the range of number you want to guess from in this format(1,100) where 1=Start and 100=End\n'
      '3) Guess until you win and if you want to give up just type the word *giveup* without spacing\n'
      '4) Goodluck!\n'
      '5) Run code in this format==> file name first name last name guessing range'
      ' e.g guessinggame.py Emmanuel Jolaiya 2 200')

# collecting name of player
first_name = sys.argv[1]
last_name = sys.argv[2]

# collecting range of guess
start = sys.argv[3]
stop = sys.argv[4]

print(f'Welcome {first_name} {last_name}, you\'ll will be guessing from {start} to {stop}..goodluck!!')
count = 0
guesses = []
give_up = 'giveup'


# validation block

while True:

    guess = input('What is your guess? ')
    count += 1
    guesses.append(guess)
    try:
        if int(guess) > int(stop) or int(guess) < int(start):

            print(f'Enter a number within the range {start} and {stop}')

        elif guess.isalpha() or guess == give_up:

            print('ensure you entered a valid integer')

        else:

            while True:

                if int(guess) != random.choice(list(range(int(start), int(stop)))):

                    print('Thats wrong, Try again')
                    computer_range=random.choice(list(range(int(start), int(stop))))
                    hint= computer_range-(int(guess))
                    print(f'hint:Your last guess + {hint} is the computers last guess')

                elif int(guess) == random.choice(list(range(int(start), int(stop)))):
                    print('You did well')
                    print('*summary statistics**\n'
                          f'guesses= {guesses}\n'
                          f'count={count} times')

                break
        continue
    except ValueError as error:

        print(
            f'Error detected: You just commited {error} Error \n'
            'That means you entered an alphabet,the only allowed words are *exit*==>to exit the code and *giveup* to'
            'see the answer. Input only valid integers please!!'
        )

    finally:

        if guess == str(give_up):
            computer = random.choice(range(int(start), int(stop)))
            print(f'I\'m sad you gave up after {int(count-1)} attempt\n'
                  f'These are your guesses so far{guesses[:-1]}\n'
                  'see you again!:)\n'
                  f'You tried but the computer\'s prediction is {computer} ')
            break

        elif guess == str('exit'):
            break






