from replit import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

dict_bid = {}

def highest_bid(bid):
    max = 0
    name = ''
    for key, value in bid.items():
        if value > max:
            max = value
            name = key    
    print(f'winner is {name} with bid {max}')

bidding_finished = False

while not bidding_finished:
    input_name = input('What is your name?: ').strip().title()
    input_bid = int(input('Your bid? $...'))
    dict_bid[input_name] = input_bid

    input_other_bid = input('Are there other bidders?: Y/N ').strip().capitalize()

    if input_other_bid != 'Y' or input_other_bid != 'N':
        print('please enter Y/N')
    
    if input_other_bid == 'Y':
        clear()
        
    
    else:
        highest_bid(dict_bid)
        bidding_finished = True
        

