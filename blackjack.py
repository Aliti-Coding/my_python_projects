import random
from functions.blackjack_func import sum21_and_11

card_score = [11,2,3,4,5,7,8,9,10,10,10,10]

 

def blackjack():
    welcome = input('hello and welcome! do you want to play one game blackjack?: (y/n): ').lower()
    if welcome == 'n':
        print('see you another time!')
        exit()   

    while True:        
        player = [random.choice(card_score), random.choice(card_score)]
        player_11 = sum21_and_11(player)
        print(f'your cards: {player_11}    and your score: {sum(player_11)}')
        dealer = [random.choice(card_score)]
        print(f'dealers card: {dealer}  and score: {sum(dealer)}')

        while True:
            player_input = input("if you want to hit type 'y', or if you want to stand type 'n': ")
            if player_input == 'y':
                player_11.append(random.choice(card_score))
                print(f'your cards: {player_11}    and your score: {sum(player_11)}')
            if sum(player_11) > 21:
                break
            elif player_input == 'n':
                print(f'your cards: {player_11}    and your score: {sum(player_11)}')
                break
            # print(f'your cards: {player}    and your score: {sum(player)}')
        
        
        #dealer cards
        dealer.append(random.choice(card_score))
        dealer_11 = sum21_and_11(dealer)
        if sum(dealer_11) < 15:
            dealer_11.append(random.choice(card_score))
            print(f'dealers card: {dealer_11}  and score: {sum(dealer_11)}')
        elif sum(dealer_11) < 20:
            print('dealer stand')
            print(f'dealers card: {dealer_11}  and score: {sum(dealer_11)}')


        #who is winner?
        if sum(player_11) > 21:
            print(f'you lose, score: {sum(player_11)}')
            
        elif sum(player_11) > sum(dealer_11):
            print('player wins!')
            
        elif sum(player_11) == sum(dealer_11):
            print('dealer wins!')
            
        elif sum(dealer_11) > 21 and sum(player_11) < 21:
            print('player wins!')

        else:
            print('dealer wins!')



        play_again = input('Do you want to play again?: (y/n): ').lower()
        if play_again == 'y':
            blackjack()
        else:
            print('thank you for the game')
            break


blackjack()