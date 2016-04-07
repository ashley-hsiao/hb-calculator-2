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

    operation = tokens[0]
    num1 = float(tokens[1])

    try:
        num2 = float(tokens[2])
    except IndexError:
        pass
        
    if operation == "q": 
        quit()

    else:
        if operation == "+": 
            output = add(num1, num2)
            print output
    
        elif operation == "-": 
            output = subtract(num1, num2)
            print output
    
        elif operation == "*": 
            output = multiply(num1, num2)
            print output
    
        elif operation == "/": 
            output = divide(num1, num2)
            print output
    
        elif operation == "square": 
            output = square(num1)
            print output
    
        elif operation == "cube": 
            output = cube(num1)
            print output    
    
        elif operation == "pow": 
            output = pow(num1, num2)
            print output
    
        elif operation == "mod": 
            output = mod(num1, num2)
            print output    
    
        # else:
        #     print "That is not a valid input, try again."
