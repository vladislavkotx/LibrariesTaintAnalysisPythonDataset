import os


def sink1(my_list):
    """A vulnerable function that executes system commands."""
    os.system(my_list) # FLAW: tainted flow to sink


def sink2(my_list):
    """A vulnerable function that executes system commands."""
    os.system(my_list) # NO FLAW


def sink3(my_list):
    """A vulnerable function that executes system commands."""
    os.system(my_list) # NO FLAW


def sink4(my_list):
    """A vulnerable function that executes system commands."""
    os.system(my_list) # NO FLAW


def sink5(my_list):
    """A vulnerable function that executes system commands."""
    os.system(my_list) # NO FLAW