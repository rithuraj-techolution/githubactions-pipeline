
from colorama import Fore, init

# Initialize colorama for automatic resetting of color
init(autoreset=True)

def print_colored_message(message, color):
    """
    Print the given message in the specified color.

    :param message: The message to print
    :param color: The color in which the message should be printed
    """
    print(color + message)

# Print "Hello World" in red
print_colored_message("Hello World", Fore.RED)
