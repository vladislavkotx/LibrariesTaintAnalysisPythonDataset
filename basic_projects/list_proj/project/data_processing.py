def create_list1(taint_var):
    """Creates the first list using the tainted variable."""
    my_list1 = []
    my_list1.append(taint_var)
    return my_list1


def create_list2(taint_var):
    """Creates the second list and counts tainted variable encounters in it."""
    my_list2 = ["data1", "data2"]
    my_list2.count(taint_var)
    return my_list2


def create_list3(taint_var):
    """Creates the third list using the tainted variable and clearing it"""
    my_list3 = []
    my_list3.append(taint_var)
    my_list3.clear()
    return my_list3


def create_list4(taint_var):
    """Creates the fourth list and uses the tainted variable as an index."""
    my_list4 = []
    my_list4.index(taint_var)
    return my_list4


def create_list5(taint_var):
    """Creates the fifth list and removes the tainted variable from it."""
    my_list5 = []
    my_list5.remove(taint_var)
    return my_list5