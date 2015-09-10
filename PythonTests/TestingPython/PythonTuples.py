'''
Created on Sep 10, 2015

@author: Meglena
'''
myList = [1,2,3]
myList.append(4)
print (myList)

myTuple = (1,2,3)
print (myTuple)

myTuple2 = (1,2,3)
myTuple2.append(4)
print (myTuple2)


#    results ARE: 
#    myTuple2.append(4) AttributeError: 'tuple' object has no attribute 'append'
#    [1, 2, 3, 4]   <= list
#    (1, 2, 3)      <= tuple
