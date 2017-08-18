'''
Created on 21 Jul 2017

@author: it
'''
#x = l^k % m
from decimal import *
def descret(n,l,k,m):
    return n*l**k%m
    

r=765
k=853
   
print(descret(1,2, 765, 2579))
print(descret(1,2,853,2579))

#计算密文
print("encrypt:",descret(1299,949,853,2579))  #2396
print("decrypt:",4**2**(-1))
print("decrypt:",descret(2396,435,765,2579))

