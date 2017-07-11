'''
Created on 10 Jul 2017

@author: it
'''

class MyClass(object):
    '''
    list for learning
    '''


    def __init__(self, params):
        print (params);
        list1 = ['physics', 'chemistry', 1997, 2000];

        print (list1);
        del (list1[2]);
        print ("After deleting value at index 2 : ")
        print (list1);
        
t = MyClass("passed param")
        