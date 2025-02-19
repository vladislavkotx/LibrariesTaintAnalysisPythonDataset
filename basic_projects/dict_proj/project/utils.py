import os


def sink1(my_dict):
    """A vulnerable function that executes system commands."""
    os.system(my_dict) # FLAW: tainted flow to sink


def sink2(my_dict):
    """A vulnerable function that executes system commands."""
    os.system(my_dict) # NO FLAW


def sink3(my_dict):
    """A vulnerable function that executes system commands."""
    os.system(my_dict) # NO FLAW