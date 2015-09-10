'''
Created on Sep 10, 2015

@author: Meglena
'''

def exceptionControl():
    yoursmart = False #boolean in Python! We can also use "0" instead of "False" and "1" instead of "True" 
    while (yoursmart == False):
        try:
            a=int(input("Tell me your age: "))
            print("You were born in the year - ", 2015-a)
            yoursmart = True
        except:
            print("You gave me a string / You did not enter a integer")    
           
exceptionControl()

#    it will keep ask us for a integer until we enter integer 