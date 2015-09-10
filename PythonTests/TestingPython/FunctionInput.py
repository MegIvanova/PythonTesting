'''
Created on Sep 10, 2015

@author: Meglena
'''


a = float(input("Tell me your test score: "))
b = float(input("What is your second test score: "))
def someFunction():
    print (a+b)
    
    #print(int(a)+int(b)) # it's not the correct way 
    #if we add the score 55.0 it will not work error
someFunction()

#   a = int(input("Tell me your test score: ")) / b = int(input("What is your second test score: "))
#   Tell me your test score: 2 / What is your second test score: 2 / result is 4

def someFunction2():
    #c=a*b
    c=a+b
    return c # i am done with the function, send the function 
    #print(c)
#someFunction2()

#    #c=a*b / a = int(input("Tell me your test score: ")) / b = int(input("What is your second test score: "))
#    Tell me your test score: 2 / What is your second test score: 5 / result1 is 7 / result2 10 

def avg2numbers():
    d=someFunction2()/2
    print(d)

avg2numbers()

#   result is Tell me your test score: 50 / What is your second test score: 50 / result1 is 100.0 / result2 is 50.0