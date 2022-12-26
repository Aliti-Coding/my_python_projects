#making my first hangman
import random
import functions

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










