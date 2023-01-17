import os
import sys
import ast

def clear():
    clear = os.system('cls')

def open_file(name):             
    fo = open(name +'.txt','r')  
    reading = fo.read()         
    dictionary = ast.literal_eval(reading)  
    fo.close()                   
    return dictionary

# Add data
# update data
# delete data