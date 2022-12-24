import random
import functions
#making my first hangman


lst_words = ["bambus", "phone", "elephant"]
random_word = random.choice(lst_words)
len_random_word = len(random_word)
covered_word_lst = list('_' * len_random_word)


attempts = 6

while True:
    letter_guessed = input('Guess a letter: ').lower()

    for idx, letter in enumerate(random_word):
        if letter_guessed == letter:
            covered_word_lst[idx] = letter_guessed        

    covered_word_str = "".join(covered_word_lst)
    print(f'{covered_word_str} \n')
    if covered_word_str in random_word:
        print("you win! Congratulations!")
        break

    if letter_guessed not in random_word:
        attempts -= 1
        print(attempts)
        print(functions.stages[attempts])

    if attempts == 0:
        print(f'Gameover! Correct word was: {"".join(random_word)} :D')
        break



    # def vizualize(num):
    #     if attempts == 5:
    #         print(head)
    #     elif attempts == 4:
    #         print(head)
    #         print(rightarm)
    #     elif attempts == 3:
    #         print(head)
    #         print(leftarm, body)
    #     elif attempts ==2:
    #         print(head)
    #         print(leftarm, body, rightarm)
    #     elif attempts ==1:
    #         print(head)
    #         print(rightarm, body, leftarm)
    #         print(leftleg)
    #     elif attempts ==0:
    #         print(head)
    #         print(rightarm, body, leftarm)
    #         print(leftleg, rightleg)
    
    # print('\n')
    # vizualize(attempts)









# my_hangman ='''
#      O
#     /|\ 
#     / \ 
# '''


# print(my_hangman)