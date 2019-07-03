print ('Hello World')           #outouts to the console
variable = 'Hello World2'         # how to set a variable
print (variable)                #prints the variable -

# [] for a list, {} for dictionaries

name = 'Sam'
if name == 'Sam':
    print('Great name')                 #use 4 spaces to indent
elif name == 'Jacob':
    print('Great guy')
else:                               #: signifies its the end of the line
    print('Oh dear...')


for i in range(5):          # for loop will print 01234
    print (i)

for i in ['a','b','c','d']:     # Will print each of the item in a list, if a string will print each character
    print(i)

my_list = []

for i in range(5):              # will put 0,1,2,3,4 in the list
    my_list.append(i)

print(my_list)      #out the loop will onlt print the once

#functions

def my_function(a_string):              # def defines the function
    print(a_string)

my_function('Hello')

def my_function(a_string):              # can use both but as its a function its supposed to return something
    return a_string

print(my_function('Hello2'))

#libaries

import math             #only needs to be imported the once at the top of the code
print( math.tau)

import random
print(random.randint(5,10))

from random import randint      # the samw thing as above but less efficient
print (randint(5,10))

