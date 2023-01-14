import os
import ast

def clear():
    clear = os.system('cls')

def open_file(name):             
    fo = open(name +'.txt','r')  #file opening
    reading = fo.read()          #reading files type: str
    dictionary = ast.literal_eval(reading)  #converting str to dictionary
    fo.close()                   #closing the file
    return dictionary            #returning result as array of dictionary

def write_data(name,sulat):
    fo = open(name +'.txt','w')  #file opening with write mode
    fo.write(sulat)              #write the new data to text document
    fo.close()                   #closing the file
    
