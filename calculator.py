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

    tokens[1] = float(tokens[1])
    tokens[2] = float(tokens[2])

    if tokens[0] == "q": 
        quit()

    else:
        if tokens[0] == "+": 
            output = add(tokens[1], tokens[2])
            print output
    
        elif tokens[0] == "-": 
            output = subtract(tokens[1], tokens[2])
            print output
    
        elif tokens[0] == "*": 
            output = multiply(tokens[1], tokens[2])
            print output
    
        elif tokens[0] == "/": 
            output = divide(tokens[1], tokens[2])
            print output
    
        elif tokens[0] == "square": 
            output = square(tokens[1])
            print output
    
        elif tokens[0] == "cube": 
            output = cube(tokens[1])
            print output    
    
        elif tokens[0] == "pow": 
            output = pow(tokens[1], tokens[2])
            print output
    
        elif tokens[0] == "mod": 
            output = mod(tokens[1], tokens[2])
            print output    
    
        else:
            print "That is not a valid input, try again."
