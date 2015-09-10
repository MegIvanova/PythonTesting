'''
Created on Sep 8, 2015

@author: Meglena
'''

def main(): 
    print ("yes")
    print ("no")
    first=adding(1,2,3)
    second=adding(4,5,6)
    third=adding(7,8,9)
    avg(first,second,third)
    for p in range(1,5):
        avg(1,2,3)

def avg(x,y,z):
    average=(x+y+z)/3
    print(average)
    print(type(average)) # it returns to me the type of the variable / class 'float''
    
def adding(a, b, c):
    return a+b+c
    
main()  

#    result 
#    YES 
#    NO
#    15.0
#    then it prints 5 times the following code
#    <class 'float'>
#    2.0
