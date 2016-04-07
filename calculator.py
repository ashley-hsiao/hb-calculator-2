"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

def check_input(tokens):
    if len(tokens) == 3:
        calculate_number()
    else:
        print "That is not a valid input, please try again."


# Your code goes here

def calculate_number():
    while True:
        input = raw_input(">")
        tokens = input.split(" ")
        # print len(tokens)

        operation = tokens[0]

        try:
            num1 = float(tokens[1])
        except IndexError:
            pass

        try:
            num2 = float(tokens[2])
        except IndexError:
            pass

        list_of_operations = ["q", "+", "-", "*", "/", "square", "cube", "pow", "mod"]

        if operation not in list_of_operations:
            print "That is not a valid input, please try again."

        elif operation == "q": 
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
        
            