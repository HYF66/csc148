"""Lab 6: Recursion

=== CSC148 Winter 2020 ===
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains a few nested list functions for you to practice recursion.
"""
from typing import Union, List

def greater_than_all(obj: Union[int, List], n: int) -> bool:
    """Return True iff there is no int in <obj> that is larger than or
    equal to <n> (or, equivalently, <n> is greater than all ints in <obj>).

    >>> greater_than_all(10, 3)
    False
    >>> greater_than_all([1, 2, [1, 2], 4], 10)
    True
    >>> greater_than_all([], 0)
    True
    """
    if isinstance(obj, int):
        if obj >= n:
            return False
    else:
        for sublist in obj:
            greater_than_all(sublist, n)
    return True


def add_n(obj: Union[int, List], n: int) -> Union[int, List]:
    """Return a new nested list where <n> is added to every item in <obj>.

    >>> add_n(10, 3)
    13
    >>> add_n([1, 2, [1, 2], 4], 10)
    [11, 12, [11, 12], 14]
    >>> add_n([1,[1,[1]],1],10)
    [11, [11, [11]], 11]
    """
    if isinstance(obj, int):
        obj += n
        return obj
    else:
        tem = []
        for sublist in obj:
            tem.append(add_n(sublist, n))
    return tem


def nested_list_equal(obj1: Union[int, List], obj2: Union[int, List]) -> bool:
    """Return whether two nested lists are equal, i.e., have the same value.

    Note: order matters.
    You should only use == in the base case. Do NOT use it to compare
    otherwise (as that defeats the purpose of this exercise)!

    >>> nested_list_equal(17, [1, 2, 3])
    False
    >>> nested_list_equal([1, 2, [1, 2], 4], [1, 2, [1, 2], 4])
    True
    >>> nested_list_equal([1, 2, [1, 2], 4], [4, 2, [2, 1], 3])
    False
    """
    # HINT: You'll need to modify the basic pattern to loop over indexes,
    # so that you can iterate through both obj1 and obj2 in parallel.

    if isinstance(obj1, int) and isinstance(obj2, int):
        if obj1 != obj2:
            return False
        else:
            return True
    else:
        if not (isinstance(obj1, list) and isinstance(obj2, list)):
            return False
        if len(obj2) == len(obj1):
            for i in range(len(obj1)):
                return nested_list_equal(obj1[i], obj2[i])
        else:
            return False



def duplicate(obj: Union[int, List]) -> Union[int, List]:
    """Return a new nested list with all numbers in <obj> duplicated.

    Each integer in <obj> should appear twice *consecutively* in the
    output nested list. The nesting structure is the same as the input,
    only with some new numbers added. See doctest examples for details.

    If <obj> is an int, return a list containing two copies of it.

    >>> duplicate(1)
    [1, 1]
    >>> duplicate([])
    []
    >>> duplicate([1, 2])
    [1, 1, 2, 2]
    >>> duplicate([1, [2, 3]])  # NOT [1, 1, [2, 2, 3, 3], [2, 2, 3, 3]]
    [1, 1, [2, 2, 3, 3]]
    """
    # HINT: in the recursive case, you'll need to distinguish between
    # a <sublist> that is an int and a <sublist> that is a list
    # (put an isinstance check inside the loop).

    if isinstance(obj, int):
        finallist = []
        finallist.append(obj)
        finallist.append(obj)
        return finallist
    else:
        finallist = []
        for sublist in obj:
            if isinstance(sublist, int):
                finallist.append(sublist)
                finallist.append(sublist)
            else:
                finallist.append(duplicate(sublist))
        return finallist
###todo

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # import python_ta
    # python_ta.check_all()
