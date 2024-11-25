 
from colorama import Fore

# Print "Hello World" in red color and then reset the color
def print_red_message(message):
    print(Fore.RED + message + Fore.RESET)

# Main function to execute the script
if __name__ == "__main__":
    print_red_message("Hello World")
