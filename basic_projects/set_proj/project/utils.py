import os


def sink1(my_set):
    """A vulnerable function that executes system commands."""
    os.system(my_set) # FLAW: tainted flow to sink


def sink2(my_set):
    """A vulnerable function that executes system commands."""
    os.system(my_set) # NO FLAW


def sink3(my_set):
    """A vulnerable function that executes system commands."""
    os.system(my_set) # NO FLAW


def sink4(my_set):
    """A vulnerable function that executes system commands."""
    os.system(my_set) # NO FLAW