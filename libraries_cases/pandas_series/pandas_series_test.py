import os
import pandas as pd

taint_var = input()                                    # Tainted variable from user input


series1 = pd.Series([1, 3, 5, taint_var, 6, 8])
os.system(str(series1))                                # FLAW: tainted flow to sink


dict2 = {'a': 1, 'b': 2, 'c': taint_var}
series2 = pd.Series(data=dict2, index=['x', 'y', 'z'])
os.system(str(series2))                                # FLAW: tainted flow to sink


series3 = pd.Series([1, "3"])
series3.iloc[0] = taint_var
os.system(str(series3))                                # FLAW: tainted flow to sink


series4 = pd.Series()
series4.get(taint_var)
os.system(str(series4))                                # NO FLAW


series5 = pd.Series([1, 2])
series5.between(0, taint_var)
os.system(str(series5))                                # NO FLAW


series6 = pd.Series([1, 2])
series6.describe(exclude=taint_var)
os.system(str(series6))                                # NO FLAW


series7 = pd.Series([1, 2])
series7.memory_usage(deep=bool(taint_var))
os.system(str(series7))                                # NO FLAW


series8 = pd.Series([1, 2, 3, 4])
series8.nsmallest(n=int(taint_var))
os.system(str(series8))                                # NO FLAW


series9 = pd.Series([1, 2, 3, 4])
series9.nlargest(n=int(taint_var))
os.system(str(series9))                                # NO FLAW


series10 = pd.Series([1, 2, 3, 4])
series10.update(taint_var)
os.system(str(series10))                               # FLAW: tainted flow to sink
