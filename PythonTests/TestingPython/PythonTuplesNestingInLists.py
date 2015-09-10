'''
Created on Sep 10, 2015

@author: Meglena
'''

def atupple():
    Mytupple = (1,2,3)
    MyList = list(Mytupple)
    MyList.append(4)
#myList.append(5) we can add as many numbers as we want to the list
    Mytupple2=tuple(MyList)
    print("This tuple can not be change", Mytupple)
    print("So I turned it into a list and added an entry", Mytupple2)
    print("I then converted the list into a new Tupple",Mytupple)
    print (MyList)


atupple()

#    nesting a Tuple in a list in order to add a number 


#    This tuple can not be change (1, 2, 3)
#    So I turned it into a list and added an entry (1, 2, 3, 4)
#    I then converted the list into a new Tupple (1, 2, 3)
#    [1, 2, 3, 4]
