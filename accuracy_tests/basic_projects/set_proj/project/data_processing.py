def create_set1(taint_var):
    """Creates the first set using the tainted variable."""
    my_set1 = set()
    my_set1.add(taint_var)
    return my_set1


def create_set2(taint_var):
    """Creates the second set and removes the tainted variable from it."""
    my_set2 = set()
    my_set2.add(taint_var)
    my_set2.remove(taint_var)
    return my_set2


def create_set3(taint_var):
    """Creates the third set using the tainted variable and clearing it"""
    my_set3 = set()
    my_set3.add(taint_var)
    my_set3.clear()
    return my_set3


def create_set4(taint_var):
    """Creates the fourth set and discards the tainted variable from it."""
    my_set4 = set()
    my_set4.add(taint_var)
    my_set4.discard(taint_var)
    return my_set4





