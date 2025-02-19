import os


def sink1(my_tuple):
    """A vulnerable function that executes system commands."""
    os.system(my_tuple) # FLAW: tainted flow to sink


def sink2(my_tuple):
    """A vulnerable function that executes system commands."""
    os.system(my_tuple) # FLAW: tainted flow to sink


def sink3(my_tuple):
    """A vulnerable function that executes system commands."""
    os.system(my_tuple) # NO FLAW


def sink4(my_tuple):
    """A vulnerable function that executes system commands."""
    os.system(my_tuple) # NO FLAW


def sink5(my_tuple):
    """A vulnerable function that executes system commands."""
    os.system(my_tuple) # FLAW: tainted flow to sink