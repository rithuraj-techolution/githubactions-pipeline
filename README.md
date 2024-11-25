# Project Title
Hello World and Utility Functions

## Overview
This project consists of two main components. The `main.py` file is a simple script to demonstrate colored console output using Colorama. The `utils.py` file contains essential utility functions for basic arithmetic operations and a demonstration of using Pandas for data manipulation and analysis.

## File Descriptions

### File: `main.py`
- **Purpose**: Demonstrates the use of the Colorama library to print colored text to the console.
- **Functions and Features**:
  - Uses `colorama.Fore` to print "Hello World" in red to the console.
  - Resets the color after printing.
- **Dependencies**: 
  - Colorama: [Installation Guide](https://pypi.org/project/colorama/)

### File: `utils.py`
- **Purpose**: Provides utility functions for arithmetic operations and simple data manipulation using Pandas.
- **Functions and Features**:
  - **Basic Arithmetic Functions**:
    - `add(a, b)`: Returns the sum of `a` and `b`.
    - `subtract(a, b)`: Returns the result of `a` minus `b`.
    - `multiply(a, b)`: Returns the product of `a` and `b`.
    - `divide(a, b)`: Returns the division of `a` by `b`, raises an error if `b` is zero.
  - **Pandas DataFrame Operations**:
    - Creation of a sample DataFrame with columns ['Name', 'Age', 'City'].
    - Calculates the mean age.
    - Filters data where age is greater than 25.
    - Adds a new column, 'Age in 5 Years', to demonstrate column manipulation.
- **Dependencies**:
  - Pandas: [Installation Guide](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)

## Setup Instructions
1. **Install Dependencies**:
    ```bash
    pip install colorama pandas
    ```
2. Make sure all files (`main.py` and `utils.py`) are in the same directory.

## Usage Guide

### Running `main.py`
To run the main script and print "Hello World" in red, execute:
```bash
python main.py
```

### Running `utils.py`
To execute and observe the DataFrame operations:
```bash
python utils.py
```

## Examples

### `main.py` Output:
```bash
Hello World
```

### `utils.py` Output:
Displays a formatted DataFrame with calculations as described in the file.

## How the Files Relate
- `main.py` and `utils.py` are standalone files that serve different purposes. `main.py` is focused on console output styling, while `utils.py` provides foundational utilities for calculations and data manipulation.

## Contributing
Feel free to contribute by submitting issues or pull requests on the project's GitHub repository. Ensure that any added features include corresponding tests.

## License
This project is licensed under the MIT License.

## Contact
For questions or contributions, please reach out to [your-email@example.com].