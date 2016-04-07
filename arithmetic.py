def add(nums):
    """Returns sum of all inputs"""

    total = 0
    for num in nums:
        total += num
    return total


def subtract(nums):
    """Subtracts all inputs from first input"""

    total = nums[0]

    for num in nums[1:]:
        total -= num
    return total
    

# remaining functions to be fixed and tested
def multiply(num1, num2):
    """Multiplies the two inputs together"""

    return num1 * num2


def divide(num1, num2):
    """Divides the first input by the second, returning a floating point"""

    return float(num1) / float(num2)


def square(num1):
    """Returns the square of the input"""

    return num1 * num1


def cube(num1):
    """Returns the cube of the input"""

    return num1 * num1 * num1


def power(num1, num2):
    """Raises the first input to the power of the second input and returns the value."""

    return num1 ** num2


def mod(num1, num2):
    """Returns the remainder when the first input is divided by the second input."""

    return num1 % num2

