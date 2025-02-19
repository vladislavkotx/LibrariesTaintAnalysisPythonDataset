import os

taint_var = input()             # Tainted variable from user input


my_list1 = []
my_list1.append(taint_var)      
os.system(my_list1)             # FLAW: tainted flow to sink


my_list2 = ["data1", "data2"]
my_list2.count(taint_var)       
os.system(my_list2)             # NO FLAW


my_list3 = []
my_list3.append(taint_var)      
my_list3.clear()                
os.system(my_list3)             # NO FLAW


my_list4 = []
my_list4.index(taint_var)       
os.system(my_list4)             # NO FLAW


my_list5 = []
my_list5.remove(taint_var)
os.system(my_list5)             # NO FLAW