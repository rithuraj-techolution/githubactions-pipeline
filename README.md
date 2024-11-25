# Project Title: Console Utilities and Data Analysis

## Overview
This project combines a console-based greeting with basic mathematical and data processing utilities. It includes functionalities for printing colored text in the terminal, performing basic arithmetic operations, and manipulating a simple dataset using pandas.

## File Descriptions

### File: `main.py`
- **Purpose**: Prints a "Hello World" message in red text using `colorama`.
- **Functions and Features**: 
  - Uses `Fore.RED` from `colorama` to display the text in red.
- **Dependencies**: 
  - `colorama` library. You can install it via `pip install colorama`.

### File: `utils.py`
- **Purpose**: Contains simple arithmetic functions for educational or basic computational use.
- **Functions and Features**:
  - `add(a, b)`: Returns the sum of `a` and `b`. 
  - `subtract(a, b)`: Returns the difference between `a` and `b`.
  - `multiply(a, b)`: Returns the product of `a` and `b`.
  - `divide(a, b)`: Returns the quotient of `a` and `b`; raises a `ValueError` if `b` is `0`.
- **Dependencies**: None.

### File: `data_analysis.py`
- **Purpose**: Demonstrates basic data manipulation using pandas.
- **Functions and Features**:
  - Creation of a sample DataFrame including names, ages, and cities.
  - Calculation of mean age.
  - Filtering of entries with age > 25.
  - Adds a new column "Age in 5 Years".
- **Dependencies**: 
  - `pandas` library. Install it via `pip install pandas`.

## Setup Instructions
1. **Install Dependencies**:
   - First, ensure you have Python installed.
   - Run the following commands to install required libraries:
     ```bash
     pip install colorama pandas
     ```

## Usage Guide
- **Run `main.py`**:
  ```bash
  python main.py
  ```
  This will output a red "Hello World" in your terminal.
  
- **Run `utils.py` with sample inputs**:
  - Example to add numbers:
    ```python
    from utils import add
    print(add(2, 3))
    ```
  
- **Run `data_analysis.py`**:
  ```bash
  python data_analysis.py
  ```
  This will showcase the sample DataFrame and operations performed on it, such as calculating the mean age and filtering data.

## Examples
- Adding numbers using `utils.py`:
  ```python
  from utils import add
  result = add(5, 7)  # Outputs: 12
  ```

## How the Files Relate
- The `main.py` file is independent and focuses on terminal text display.
- The `utils.py` contains arithmetic functions that can be used in other projects for calculations.
- The `data_analysis.py` uses pandas for data manipulation, showcasing different capabilities compared to simple arithmetic in `utils.py`.

## Contributing
Feel free to fork the repository and submit pull requests. Ensure your code is well-documented and follows the project's coding standards.

## License
This project is open-source and available under the MIT License.

## Contact
For questions or contributions, please contact dev@example.com.