import os
import pandas as pd

taint_var = input()  # Tainted variable from user input


data1 = {
    "A": [1, 3, 5],
    "B": [5.5, 6, 8]
}
df1 = pd.DataFrame(data1, index=[taint_var, "day2", "day3"])
os.system(str(df1))                                          # FLAW: tainted flow to sink


data2 = {
    "A": [1, 3, 5],
    "B": [5.5, 6, 8]
}
df2 = pd.DataFrame(data2)
df2.update({'B': [taint_var, 7, 9]})
os.system(str(df2))                                          # FLAW: tainted flow to sink


data3 = {
    "A": [1, 3, 5],
    "B": [5.5, 6, 8]
}
df3 = pd.DataFrame(data3)
df3.iloc[0] = taint_var
os.system(str(df3))                                          # FLAW: tainted flow to sink


df4 = pd.DataFrame()
df4.get(taint_var)
os.system(str(df4))                                          # NO FLAW


data5 = {
    "A": [1, 3, 5],
    "B": [5.5, 6, 8]
}
df5 = pd.DataFrame(data5)
df5.describe(exclude=taint_var)
os.system(str(df5))                                          # NO FLAW


data6 = {
    "A": [1, 3, 5],
    "B": [5.5, 6, 8]
}
df6 = pd.DataFrame(data6)
df6.memory_usage(deep=bool(taint_var))
os.system(str(df6))                                          # NO FLAW


data7 = {
    "A": [1, 3, 5],
    "B": [5.5, 6, 8]
}
df7 = pd.DataFrame(data7)
df7.nsmallest(3, columns=taint_var)
os.system(str(df7))                                          # NO FLAW


data8 = {
    "A": [1, 3, 5],
    "B": [5.5, 6, 8]
}
df8 = pd.DataFrame(data8)
df8.nsmallest(3, columns=taint_var)
os.system(str(df8))                                          # NO FLAW


data9 = {
    "A": [1, 3, 5],
    "B": [5.5, 6, 8]
}
df9 = pd.DataFrame(data9)
df9.pop(taint_var)
os.system(str(df9))                                         # NO FLAW