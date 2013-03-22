#int between 0 - 100.
#program is to guess based on user input for higher (h), lower (l) or correct (c)

#First guess will be 50.
minRange = 0
maxRange = 100
guess = (minRange + maxRange) / 2
print('Please think of a number between 0 and 100!')
promptString = "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."
print('Is your secret number {0}?'.format(guess))
test = raw_input(promptString)
while test != 'c':
    if test == 'l':
        minRange = guess
    elif test == 'h':
        maxRange = guess
    else:
        print('Sorry, I did not understand your input.')
    guess = (minRange + maxRange) / 2
    print('Is your secret number {0}?'.format(guess))
    test = raw_input(promptString)

print('Game over. Your secret number was: {0}'.format(guess))
