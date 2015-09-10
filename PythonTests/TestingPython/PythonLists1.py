'''
Created on Sep 10, 2015

@author: Meglena
'''


'''def alist():
    Mylist=[5,7,9,"Bob", "Apple", 11,15.0]
    for a in Mylist:
        print(type(a))
alist()'''

# print(a) it prints => 5 7 9 Bob Apple 11 15.0 
# print(type(a))  it prints => <class 'int'>  <class 'int'>  <class 'int'>  <class 'str'> <class 'str'> <class 'int'>  <class 'float'>

'''def alist():
    Mylist=[5,7,9,"Bob", "Apple", 11,15.0]
#for a in Mylist:
    #print(a)
        
        
    Mylist.reverse()
    print("")
    print('BREAK')
    for a in Mylist:
        print(a)
alist()'''

# reverse - reverses elements in the list; result =>  BREAK  15.0   11  Apple  Bob  9  7  5

'''def alist():
    Mylist=[5,7,9,"Bob", "Apple", 11,15.0]
       
    Mylist.pop()
    print("")
    print('BREAK')
    for a in Mylist:
        print(a)
alist()'''


# Mylist.pop() with no index removes the last one which is 15.0 in this case
# Mylist.pop(Bob) it will remove Bob from the List

def alist():
    Mylist=[5,7,9,"Bob", "Apple", 11,15.0]
       
    names=Mylist.pop(3)
    print("")
    print('BREAK')
    print("This person is a god:", names)
    for a in Mylist:
        print(a)
alist()


# result => BREAK This person is a god: Bob  5  7  9  Apple  11  15.0
