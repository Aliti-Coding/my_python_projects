import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_input = int(input("type 0 for rock, 1 for paper and 2 for scissors: "))
if user_input >= 3 or user_input < 0:
    print('invalid number, please enter number between 0 and 2!')
else: 

    var = [rock, paper, scissors]

    user_chose = var[int(user_input)]

    random_gen = random.randint(0, len(var) -1)
    random_rps = var[random_gen]


    if user_chose == rock:
        if random_rps == paper:
            print(f"you chose: {user_chose}")
            print(f"computer chose: {random_rps}")
            print('You lose')
        elif random_rps == user_chose:
            print(f'its a even. computer chose: {random_rps} . you chose: {user_chose} .')
        
        else:
            print(f'you won, computer chose: {random_rps}. you chose: {user_chose}.')

    if user_chose == paper:
        if random_rps == scissors:
            print(f"you chose: {user_chose} ")
            print(f"computer chose: {random_rps}")
            print('You lose')
        elif random_rps == user_chose:
            print(f'its a even. computer chose: {random_rps}. you chose: {user_chose}.')
        
        else:
            print(f'you won, computer chose: {random_rps}. you chose: {user_chose}.')


    if user_chose == scissors:
        if random_rps == rock:
            print(f"you chose: {user_chose}")
            print(f"computer chose: {random_rps}")
            print('You lose')
        elif random_rps == user_chose:
            print(f'its a even. computer chose: {random_rps}. you chose: {user_chose}.')
        
        else:
            print(f'you won, computer chose: {random_rps}. you chose: {user_chose}.')





