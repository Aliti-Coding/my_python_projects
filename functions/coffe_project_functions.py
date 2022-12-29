#coffee_ report

def coffee_report(water, milk, coffee, money):
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")



#money functions
def quarters(num):
    """ Mulitplies number of quareters 
    with 0.25

    Args:
        num (int): _description_

    Returns:
        Float: _description_
    """
    return float(num*0.25)

def dimes(num):
    """ Mulitplies number of dimes 
    with 0.10

    Args:
        num (int): _description_

    Returns:
        Float: _description_
    """
    return float(num*0.10)

def nickel(num):
    """ Mulitplies number of nickles 
    with 0.05

    Args:
        num (int): _description_

    Returns:
        Float: _description_
    """
    return float(num*0.05)

def pennie(num):
    """ Mulitplies number of pennies 
    with 0.01

    Args:
        num (int): _description_

    Returns:
        Float: _description_
    """
    return float(num*0.01)
