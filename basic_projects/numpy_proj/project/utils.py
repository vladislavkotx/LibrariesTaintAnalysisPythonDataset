import os


def sink1(array):
    """A vulnerable function that executes system commands."""
    os.system(array) # FLAW: tainted flow to sink


def sink2(array):
    """A vulnerable function that executes system commands."""
    os.system(array) # NO FLAW


def sink3(array):
    """A vulnerable function that executes system commands."""
    os.system(array) # NO FLAW


def sink4(array):
    """A vulnerable function that executes system commands."""
    os.system(array) # FLAW: tainted flow to sink