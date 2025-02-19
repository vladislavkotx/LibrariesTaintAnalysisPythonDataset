import numpy as np
import os

taint_var = input()                                       # Tainted variable from user input


array1 = np.array([taint_var])
os.system(array1)                                         # FLAW: tainted flow to sink


array2 = np.array([1, 2, 3, 4])
index = int(taint_var)
value = array2[index]
os.system(array2)                                         # NO FLAW


array3 = np.array([1, 2, 3])
array3.reshape((3, taint_var))
os.system(array3)                                         # NO FLAW


array4 = np.array([1, 2])
tainted_array = np.array([taint_var])
combined_array = np.concatenate((array4, tainted_array))
os.system(combined_array)                                 # FLAW: tainted flow to sink
