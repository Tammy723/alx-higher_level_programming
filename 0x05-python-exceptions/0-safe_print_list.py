#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x number of elememts from a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    ret = 0
    for n in range(x):
        try:
            print("{}".format(my_list[n]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
