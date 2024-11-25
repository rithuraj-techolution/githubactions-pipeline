# Project Title: Simple Python Utility and DataFrame Project

## Overview
This project consists of two main parts: a simple script utilizing color printing features and a utility module providing basic arithmetic operations and DataFrame manipulation. The project demonstrates how to perform colored output in a terminal and manage data using Pandas, making it a useful tool for small data processing tasks and console applications.

## File Descriptions

### 1. `main.py`
- **Purpose**: Demonstrates the use of the `colorama` library to print text in color in the console.
- **Functions and Features**:
  - Prints "Hello World" in red text in the terminal.
- **Dependencies**: Requires the `colorama` library. (Install via `pip install colorama`)

### 2. `utils.py`
- **Purpose**: Provides basic arithmetic operations and examples of Pandas DataFrame manipulation.
- **Functions and Features**:
  - **Arithmetic Operations**:
    - `add(a, b)`: Returns the sum of `a` and `b`.
    - `subtract(a, b)`: Returns the difference of `a` and `b`.
    - `multiply(a, b)`: Returns the product of `a` and `b`.
    - `divide(a, b)`: Returns the division of `a` by `b`, raises error if `b` is zero.
  - **Pandas DataFrame Example**:
    - Creates a DataFrame with columns 'Name', 'Age', and 'City'.
    - Calculates the mean age.
    - Filters rows where age is greater than 25.
    - Adds a new column 'Age in 5 Years'.
- **Dependencies**: Requires the `pandas` library. (Install via `pip install pandas`)

## Setup Instructions
1. Ensure Python is installed on your system.
2. Install the required dependencies:
   ```
   pip install colorama pandas
   ```

## Usage Guide

### Running `main.py`
Execute the following command in your terminal to see the colored output:
```bash
python main.py
```

### Using `utils.py`
To perform arithmetic or DataFrame manipulations, import `utils.py` in your script or run it directly for the DataFrame example:
```bash
python utils.py
```

## Examples

### Arithmetic Example:
```python
from utils import add, subtract, multiply, divide

print(add(10, 5))         # Output: 15
print(subtract(10, 5))    # Output: 5
print(multiply(10, 5))    # Output: 50
print(divide(10, 5))      # Output: 2.0
```

### DataFrame Manipulation:
The DataFrame will output with calculated mean age and new columns as shown in the scripts print statements.

## How the Files Relate
- `main.py` is standalone and demonstrates simple color printing.
- `utils.py` combines arithmetic functions and data manipulation in one place, providing support for basic data operations.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with enhancements or bug fixes.

## License
This project is licensed under the MIT License.

## Contact
For questions or suggestions, please contact [your-email@example.com].