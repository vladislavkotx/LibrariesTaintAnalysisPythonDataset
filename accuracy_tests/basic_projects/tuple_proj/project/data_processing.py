def create_tuple1(taint_var):
    """Creates the first tuple using the tainted variable."""
    tup1 = (taint_var,)
    return tup1


def create_tuple2(taint_var):
    """Creates the second tuple using the tainted variable."""
    tup2 = ("data1", "data2") + (taint_var,)
    return tup2


def create_tuple3(taint_var):
    """Creates the third tuple and counts tainted variable encounters in it."""
    tup3 = ("data1", "data2")
    tup3.count(taint_var)
    return tup3


def create_tuple4(taint_var):
    """Creates the fourth tuple and uses the tainted variable as an index."""
    tup4 = ("data1", "data2")
    tup4.index(taint_var)
    return tup4


def create_tuple5(taint_var):
    """Creates the fifth tuple and discards the tainted variable from it."""
    tup5 = ("data1", taint_var)
    return tup5
