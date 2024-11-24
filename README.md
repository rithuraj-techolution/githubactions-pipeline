# Project Title: Standalone Scripts Collection

## Overview

This project consists of multiple standalone Python scripts, each serving distinct purposes, from printing colored text to performing arithmetic and data analysis operations. The primary goal is to provide modular and reusable code pieces that can be easily integrated into larger applications or used for educational purposes.

## File Descriptions

### File: `main.py`
- **Purpose**: Prints colored "Hello World" to the console.
- **Functions and Features**:
  - Utilizes the `colorama` library to print text in red color.
- **Dependencies**: 
  - `colorama` library.
  
### File: `utils.py`
- **Purpose**: Contains utility functions for basic arithmetic operations and data manipulation using pandas.
- **Functions and Features**:
  - **Arithmetic Operations**:
    - `add(a, b)`: Returns the sum of `a` and `b`.
    - `subtract(a, b)`: Returns the difference of `a` and `b`.
    - `multiply(a, b)`: Returns the product of `a` and `b`.
    - `divide(a, b)`: Returns the quotient of `a` and `b` with a check for division by zero.
  - **Pandas DataFrame Operations**:
    - Creates a sample DataFrame and performs operations like calculating the mean age, filtering, and adding new columns.
- **Dependencies**:
  - `pandas` library.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/rithuraj-techolution/githubactions-pipeline.git
   ```
2. Navigate into the project directory:
   ```bash
   cd githubactions-pipeline
   ```
3. Install the required dependencies:
   ```bash
   pip install colorama pandas
   ```

## Usage Guide

### Running `main.py`
- Command: 
  ```bash
  python main.py
  ```
- Expected Output: "Hello World" printed in red color.

### Running Arithmetic Functions in `utils.py`
- Example usage in a Python shell:
  ```python
  from utils import add, subtract, multiply, divide
  result = add(2, 3)  # Outputs: 5
  ```

### Running Data Operations in `utils.py`
- Command to display DataFrame:
  ```bash
  python utils.py
  ```

## Examples

### Arithmetic Example
```python
from utils import divide

try:
    print(divide(10, 2))  # Outputs: 5.0
    print(divide(10, 0))  # Raises ValueError
except ValueError as e:
    print(e)
```

### DataFrame Example
- Filter rows where age is greater than 25:
  ```python
  # Code within `utils.py` will showcase this when run
  ```

## How the Files Relate

The files are independent; `main.py` is primarily for demonstrating colored text output, while `utils.py` provides utility functions and data manipulation examples separately.

## Contributing

To contribute, fork the repository and submit a pull request. Ensure code quality by adhering to Python's PEP 8 standards. New utility functions can be added to `utils.py`, and enhancements to existing scripts are welcome.

## License

This project is distributed under the MIT License.

## Contact

For questions or contributions, reach out to Rithuraj Nambiar at [rithuraj.nambiar@techolution.com](mailto:rithuraj.nambiar@techolution.com).