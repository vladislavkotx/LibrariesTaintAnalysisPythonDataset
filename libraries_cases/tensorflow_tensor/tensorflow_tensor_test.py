import tensorflow as tf
import os

taint_var = input()  # Tainted variable from user input


tensor1 = tf.constant([2.0, float(taint_var), 4.0])
os.system(str(tensor1))                                  # FLAW: tainted flow to sink


tensor2 = tf.data.Dataset.from_tensor_slices([1, taint_var, 3])
os.system(str(tensor2))                                  # FLAW: tainted flow to sink


tensor3 = tf.data.Dataset.from_tensor_slices([1, 2, 3])
tensor3.skip(count=taint_var)
os.system(str(tensor3))                                  # NO FLAW


dataset4 = tf.data.Dataset([1, taint_var, 3])
os.system(str(dataset4))                                 # FLAW: tainted flow to sink


dataset5 = tf.data.Dataset([1, 2, 3])
dataset5.skip(count=taint_var)
os.system(str(dataset5))                                 # NO FLAW

