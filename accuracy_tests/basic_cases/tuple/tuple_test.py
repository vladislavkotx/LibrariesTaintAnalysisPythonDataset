import os

taint_var = input()                        # Tainted variable from user input


tup1 = taint_var
os.system(tup1)                            # FLAW: tainted flow to sink


tup2 = ("data1", "data2") + (taint_var,)
os.system(tup2)                            # FLAW: tainted flow to sink


tup3 = ("data1", "data2")
tup3.count(taint_var)
os.system(tup3)                            # NO FLAW


tup4 = ("data1", "data2")
tup4.index(taint_var)
os.system(tup4)                            # NO FLAW


tup5 = ("data1", taint_var)
os.system(tup5)                            # FLAW: tainted flow to sink