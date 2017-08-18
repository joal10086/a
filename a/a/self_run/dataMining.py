'''
Created on 29 Jul 2017

@author: it
'''
import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
#from sklearn import  *  #机器学习库
np.random.seed(123) #设置随机数种子

iris = pd.read_csv("D:\\PythonFiles\\IRIS.csv")

print (iris.shape)
print (iris.head())