import os

taint_var = input()                                    # Tainted variable from user input


my_dict1 = {}
my_dict1['key'] = taint_var
os.system(my_dict1)                                    # FLAW: tainted flow to sink


my_dict2 = {'data1': 'value1', 'data2': 'value2'}
my_dict2.get(taint_var, 'default')
os.system(my_dict2)                                    # NO FLAW


my_dict3 = {}
my_dict3['key'] = taint_var
my_dict3.clear()
os.system(my_dict3)                                    # NO FLAW