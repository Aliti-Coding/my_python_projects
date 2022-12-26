
def sum21_and_11(lst):
    """returns a lst with 1ns instead of 11
    if the score is above 21

    Args:
        lst (_list_): _description_

    Returns:
        _list_: _with 1ns instead of 11_
    """
    if sum(lst) > 21 and 11 in lst:
        idx = lst.index(11)
        lst[idx] = 1
    return lst

