def create_dict1(taint_var):
    """Creates the first dict using the tainted variable."""
    my_dict1 = {}
    my_dict1['key'] = taint_var
    return my_dict1


def create_dict2(taint_var):
    """Creates the second dict and uses the tainted variable as key to get item."""
    my_dict2 = {'data1': 'value1', 'data2': 'value2'}
    my_dict2.get(taint_var, 'default')
    return my_dict2


def create_dict3(taint_var):
    """Creates the third dict using the tainted variable and clearing it"""
    my_dict3 = {}
    my_dict3['key'] = taint_var
    my_dict3.clear()
    return my_dict3