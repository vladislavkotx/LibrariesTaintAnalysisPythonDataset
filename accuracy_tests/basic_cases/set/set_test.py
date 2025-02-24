import os

taint_var = input()           # Tainted variable from user input


my_set1 = set()
my_set1.add(taint_var)
os.system(my_set1)            # FLAW: tainted flow to sink


my_set2 = set()
my_set2.add(taint_var)
my_set2.remove(taint_var)
os.system(my_set2)            # NO FLAW


my_set3 = set()
my_set3.add(taint_var)
my_set3.clear()
os.system(my_set3)            # NO FLAW


my_set4 = set()
my_set4.add(taint_var)
my_set4.discard(taint_var)
os.system(my_set4)            # NO FLAW


