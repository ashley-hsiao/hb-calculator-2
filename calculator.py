"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *
# Your code goes here


while True:
    input = raw_input(">")
    list_of_inputs = input.split(" ")

    operation = list_of_inputs[0]
    string_of_nums = list_of_inputs[1:]

    nums = [float(i) for i in string_of_nums]

    if operation == "+": 
        output = add(nums)
        print output

    elif operation == "-": 
        output = subtract(nums)
        print output
        
#     try:
#         num1 = float(list_of_inputs[1])
#     except IndexError:
#         pass

#     try:
#         num2 = float(list_of_inputs[2])
#     except IndexError:
#         pass

#     list_of_operations = ["q", "+", "-", "*", "/", "square", "cube", "pow", "mod"]

#     if operation not in list_of_operations:
#         print "That is not a valid input, please try again."

#     elif operation == "q": 
#         quit()

#     else:
#         if operation == "+": 
#             output = add(nums)
#             print output
    
#         elif operation == "-": 
#             output = subtract(num1, num2)
#             print output
    
#         elif operation == "*": 
#             output = multiply(num1, num2)
#             print output
    
#         elif operation == "/": 
#             output = divide(num1, num2)
#             print output
    
#         elif operation == "square": 
#             output = square(num1)
#             print output
    
#         elif operation == "cube": 
#             output = cube(num1)
#             print output    
    
#         elif operation == "pow": 
#             output = pow(num1, num2)
#             print output
    
#         elif operation == "mod": 
#             output = mod(num1, num2)
#             print output
    
# #note - check for nums - nums[1:]
