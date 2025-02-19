import numpy as np


def create_array1(taint_var):
    """Creates the first array using the tainted variable."""
    return np.array([taint_var])


def create_array2(taint_var):
    """Creates the second array and uses the tainted variable as an index."""
    array2 = np.array([1, 2, 3, 4])
    index = int(taint_var)
    value = array2[index]
    return array2


def create_array3(taint_var):
    """Creates the third array and uses the tainted variable for reshaping"""
    array3 = np.array([1, 2, 3])
    try:
        array3.reshape((3, int(taint_var)))
    except ValueError:
        pass
    return array3


def create_array4(taint_var):
    """Creates the fourth array and concatenates it with a tainted array."""
    array4 = np.array([1, 2])
    tainted_array = np.array([taint_var])
    combined_array = np.concatenate((array4, tainted_array))
    return combined_array