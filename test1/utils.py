
def add(a, b):
    """
    Adds two numbers.

    Parameters:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Subtracts the second number from the first.

    Parameters:
    a (float): The number to subtract from.
    b (float): The number to subtract.

    Returns:
    float: The difference of a and b.
    """
    return a - b

def multiply(a, b):
    """
    Multiplies two numbers.

    Parameters:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The product of a and b.
    """
    return a * b

def divide(a, b):
    """
    Divides the first number by the second.

    Parameters:
    a (float): The dividend.
    b (float): The divisor.

    Returns:
    float: The quotient of a and b.

    Raises:
    ValueError: If the divisor is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    """
    Main function to test the arithmetic operations.
    """
    # Example usage of functions
    x, y = 10, 5
    
    print(f"Add: {x} + {y} = {add(x, y)}")
    print(f"Subtract: {x} - {y} = {subtract(x, y)}")
    print(f"Multiply: {x} * {y} = {multiply(x, y)}")
    print(f"Divide: {x} / {y} = {divide(x, y)}")

if __name__ == "__main__":
    main()
