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

def avg(x,y,z):
    average=(x+y+z)/3
    print(average)
    print(type(average)) # it returns to me the type of the variable / class 'float''
    
def adding(a, b, c):
    return a+b+c
    
main()   

# avg(sum(1,2,3)+sum(4,5,6)+sum(7,8,9))/3
#yes
#no 
#15.0
#<class 'float'>
