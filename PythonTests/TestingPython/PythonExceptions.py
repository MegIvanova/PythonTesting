'''
Created on Sep 10, 2015

@author: Meglena
'''

'''def exceptionControl():
    var1 = '1'
    try:
        var1 = var1 + 1 # since var1 is a string, it cannot be added to the number 1 
    except:
        print(var1, " is not a number") #so we execute this
        print(var1)
    
exceptionControl()'''

#    1  is not a number
#    1

def exceptionControl():
    
    try:
        a=int(input("Tell me your age: "))
        print("You were born in the year - ", 2015-a)
    except:
        print("You gave me a string / You did not enter a integer")
           
exceptionControl()

#    we put a number let's say 27 it will give as You were born in the year - 1988 
#    if we put 15.0 = > You gave me a string
#    if we put text = > You gave me a string


