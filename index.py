# Day 1 # 66 days of data # |||| Starts with basic - DATAQuest.io
                       # Variables and Data Types

import pandas as pd
a = 1
b = 2

c = (a + b)

print(c)


# EX 1 : # Save the result of (42 - 11) * 22 to result.
#Print result.

result = (42 -11) * 22
print (result)



# EX 2 : 

a_value = 15
a_result = (25 - 7) * 17

print(a_value)
print(12 + a_result)
print(a_value + a_result)

# Variables 
counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string


#Standard Data Types   
#Numbers         #String      #List     #Tuple       #Dictionary



#Numbers
int #(signed integers)
# long #(long integers, they can also be represented in octal and hexadecimal)
float #(floating point real values)
complex #(complex numbers)




#String
str = 'Hello World!'

print (str)         # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string




# Python Lists

list = [ 'abcd' , 786 , 2.23, 'john', 70.2 ]
print(list)

tinylist = [123, 'john']
print(tinylist)


# SLICING 
print (list)          # Prints complete list
print (list[0])       # Prints first element of the list
print (list[1:3])     # Prints elements starting from 2nd till 3rd 
print (list[2:])      # Prints elements starting from 3rd element
print (tinylist * 2)  # Prints list two times
print (list + tinylist) # Prints concatenated lists


#Python Tuples
#A tuple is another sequence data type that is similar to the list. 
##A tuple consists of a number of values separated by commas. Unlike lists, 
#however, tuples are enclosed within parentheses.
#The main differences between lists and tuples are: Lists are enclosed in brackets ( [ ] ) 
#and their elements and size can be changed, while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. 
#Tuples can be thought of as read-only lists. 


tuple = ( 'hijk', 123 , 4.46, 'j', .20  )
print(tuple)
tinytuple = (123, 'john')
print(tinytuple)

tuple = 1000
print(tuple)


#Python Dictionary

#Python's dictionaries are kind of hash table type. 
# They work like associative arrays or hashes found in Perl and consist of key-value pairs. 
# A dictionary key can be almost any Python type, but are usually numbers or strings. 
# Values, on the other hand, can be any arbitrary Python object.
#Dictionaries are enclosed by curly braces ({ }) and values can be assigned and accessed using square braces ([])


dict = {}
dict['one'] = "one"
dict[2] = "two"
tinydict = {'name':'John', 'code':6734, 'dept':'sales'}

print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

