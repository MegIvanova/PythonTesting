'''
Created on Sep 8, 2015

@author: Meglena
'''
#Python Program to Print all factorials Numbers in an Interval 0 to 20

def main(): 
    f = 1
    n = 0
    for a in range (0,20):
        n += 1
        f = f * n
        print(n,"! = ",f)
 
main()

# prints all factorials from 1 to 20 