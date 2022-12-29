from functions.coffe_project_data import MENU, resources
import functions.coffe_project_functions as coffefunc



#TODO: 2. check resources sufficient to make the drink order

water = resources['water']
milk = resources['milk']
coffee = resources['coffee']
money = 0


def coffe_selected(name):
    
    water_c = 0
    milk_c = 0
    coffee_c = 0
    if 'water' in MENU[name]['ingredients']:
        water_c = MENU[name]['ingredients']['water']
    if 'milk' in  MENU[name]['ingredients']:
        milk_c = MENU[name]['ingredients']['milk']  
    if 'coffee' in MENU[name]['ingredients']:
        coffee_c = MENU[name]['ingredients']['coffee']
    return [water_c, milk_c, coffee_c]

def coffee_checker(coffee_choice):
    """Checks if there is enough coffee resources

    Args:
        coffee_choice (list): _description_

    Returns:
        _bool_: _description_
    """
    not_enough_resources = []
    enough_water = water >= coffee_choice[0]
    enough_milk = milk >= coffee_choice[1]
    enough_coffee = coffee >= coffee_choice[2]
    if enough_water == False:
        not_enough_resources.append('water')
    if enough_milk == False:
        not_enough_resources.append('milk')
    if enough_coffee == False:
        not_enough_resources.append('coffee')
    if len(not_enough_resources) >= 1:
        return ', '.join(not_enough_resources)

    else:
        return True


def user_input_money():
    pass
    print('Please insert coins')
    quarters_input = int(input('How many quarters?: '))
    total_quarters = coffefunc.quarters(quarters_input) 

    dimes_input = int(input('How many dimes?: '))
    total_dimes = coffefunc.dimes(dimes_input)

    nickles_input = int(input('How many nickles?: '))
    total_nickles = coffefunc.dimes(nickles_input)

    pennies_input = int(input('How many pennies?: '))
    total_pennies = coffefunc.pennie(pennies_input)
    total_money_input = total_quarters + total_dimes + total_nickles + total_pennies
    return total_money_input

    
def refund_money(total_quarters, total_dimes, total_nickles, total_pennies):
    """Takes money inserted from userinput. calculates the
    sum and subtracts from the coffee cost

    Args:
        total_quarters (int): _description_
        total_dimes (int): _description_
        total_nickles (int): _description_
        total_pennies (int): _description_

    Returns:
        int: _description_
    """
    total_sum = round( total_quarters + total_dimes + total_nickles + total_pennies, 2 )
    coffee_cost = MENU[user_input]['cost']
    money_refund = round(total_sum - coffee_cost, 2)
    
    if total_sum >= coffee_cost:
        return money_refund
    else:
        return total_sum


coffe_on = True


while coffe_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
    if user_input == 'off':
        coffe_on = False #bruk bool verdi istede
        continue
    #check if we have resources to make coffee
    if user_input == 'cappuccino' or user_input == 'latte' or user_input == 'espresso':
        coffee_choice = coffe_selected(user_input)
        if coffee_checker(coffee_choice) == True:
            pass
        else:
            print(f'Sorry there is not enough {coffee_checker(coffee_choice)}')
            continue
        
    elif user_input == 'report':
        coffefunc.coffee_report(water, milk, coffee, money)
        continue
        #recursion function ? start again from thhe top?


    #FINISHED! insert coins - ask how much money from each type
    coffee_cost = MENU[user_input]['cost']


    inserted_money = user_input_money()
    if inserted_money >= coffee_cost:
        print(f"Here is ${ round( inserted_money - coffee_cost, 2 ) } dollars in change.")
        print(f"Enjoy your {user_input}!")
        money += coffee_cost
        water -= coffee_choice[0]
        milk -= coffee_choice[1]
        coffee -= coffee_choice[2]
    
    else:
        print(f"Coffee cost to low. Coffee cost is: {coffee_cost}. You inserted: {inserted_money}")
    

