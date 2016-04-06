"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

# Your code goes here

while True:
    input = raw_input(">")
    tokens = input.split(" ")

    if tokens[0] == "q": 
        quit()

    else:
        if tokens[0] == "+": 
            output = add(int(tokens[1]), int(tokens[2]))
            print output
    
        elif tokens[0] == "-": 
            output = subtract(int(tokens[1]), int(tokens[2]))
            print output
    
        elif tokens[0] == "*": 
            output = multiply(int(tokens[1]), int(tokens[2]))
            print output
    
        elif tokens[0] == "/": 
            output = divide(int(tokens[1]), int(tokens[2]))
            print output
    
        elif tokens[0] == "square": 
            output = square(int(tokens[1]))
            print output
    
        elif tokens[0] == "cube": 
            output = cube(int(tokens[1]))
            print output    
    
        elif tokens[0] == "pow": 
            output = pow(int(tokens[1]), int(tokens[2]))
            print output
    
        elif tokens[0] == "mod": 
            output = mod(int(tokens[1]), int(tokens[2]))
            print output    
    
        else:
            print "That is not a valid input, try again."
