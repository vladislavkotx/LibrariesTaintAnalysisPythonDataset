import torch
import os

taint_var = input()  # Tainted variable from user input


tensor1 = torch.tensor([1, int(taint_var), 3])
os.system(str(tensor1))                  # FLAW: tainted flow to sink


tensor2 = torch.tensor((2, int(taint_var), 19))
os.system(str(tensor2))                  # FLAW: tainted flow to sink


tensor3 = torch.empty(3, int(taint_var))
os.system(str(tensor3))                  # NO FLAW


tensor4 = torch.zeros(2, int(taint_var))
os.system(str(tensor4))                  # NO FLAW


tensor5 = torch.ones(2, int(taint_var))
os.system(str(tensor5))                  # NO FLAW


torch.manual_seed(1729)
tensor6 = torch.rand(2, int(taint_var))
os.system(str(tensor6))                  # NO FLAW


a7 = torch.rand(1, 3)
b7 = torch.tensor([1.0, float(taint_var), 3.0])
c7 = torch.zeros(1)
tensor7 = torch.matmul(a7, b7, out=c7)
os.system(str(tensor7))                  # FLAW: tainted flow to sink
os.system(str(c7))                       # FLAW: tainted flow to sink