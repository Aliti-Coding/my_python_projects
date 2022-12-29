import random
random_number = random.randint(1,100)

print(random_number)
def low_high(num):
    if num > random_number:
        return 'too high'
    elif num < random_number:
        return 'too low'    
    elif num == random_number:
        return 'you guessed the number!'

# print(low_high(guess_num))

hard = 5
easy = 10

difficulty = input('choose between difficulty level, type (easy) or (hard): ').strip().lower()

while True:

    if hard == 0:
        print('game over no more attempts left')
        break
    elif easy == 0:
        print('game over  no more attempts left')
        break
    if difficulty == 'hard':
        print(f'You have attempts left remaining: {hard}')
        hard -= 1
    elif difficulty == 'easy':
        print(f'You have attempts left remaining: {easy}')
        easy -= 1

    guess_input = int(input('guess a number between 1-100: '))
    print(low_high(guess_input))
    if low_high(guess_input) == 'you guessed the number!':
        break
