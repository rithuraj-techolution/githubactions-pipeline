# Python Utility Toolset

## Overview
The Python Utility Toolset is a versatile project that combines basic arithmetic operations, data manipulation using pandas, and colorized console output to demonstrate how core Python functionalities can be enhanced with third-party libraries.

## File Descriptions

### 1. `main.py`
- **Purpose**: Provides an example of console output with enhanced visuals using color.
- **Functions and Features**: 
  - Utilizes the `colorama` library to print "Hello World" in red text.
- **Dependencies**: 
  - [`colorama`](https://pypi.org/project/colorama/) - To produce colored terminal text. 
  - **Installation**: `pip install colorama`

### 2. `utils.py`
- **Purpose**: Provides basic arithmetic operations.
- **Functions and Features**:
  - `add(a, b)`: Returns the sum of `a` and `b`.
  - `subtract(a, b)`: Returns the difference of `a` and `b`.
  - `multiply(a, b)`: Returns the product of `a` and `b`.
  - `divide(a, b)`: Returns the division of `a` by `b` and raises an error if `b` is zero.
- **Dependencies**: None

### 3. `data_utils.py`
- **Purpose**: Demonstrates data manipulation using pandas.
- **Functions and Features**:
  - Creates a DataFrame with sample data.
  - Calculates and prints the mean age.
  - Filters and displays data based on age.
  - Adds a column showing age in 5 years.
- **Dependencies**: 
  - [`pandas`](https://pandas.pydata.org/) - For data analysis and manipulation.
  - **Installation**: `pip install pandas`

## Setup Instructions
1. Clone the repository to your local machine.
2. Install required dependencies with:
   ```bash
   pip install colorama pandas
   ```

## Usage Guide

### Running Files
- **`main.py`**: Run the following command to see "Hello World" in red:
  ```bash
  python main.py
  ```

- **Arithmetic Functions (`utils.py`)**:
  - Use these functions by importing `utils.py` in your scripts:
    ```python
    from utils import add, subtract, multiply, divide

    print(add(5, 3))         # Output: 8
    print(subtract(5, 3))    # Output: 2
    ```

- **Data Operations (`data_utils.py`)**:
  ```bash
  python data_utils.py
  ```
  - **Output**: Outputs the sample DataFrame, mean age, filtered data, and updated DataFrame.

## How the Files Relate
- `main.py` shows integration with external libraries for enhanced console output.
- `utils.py` offers standalone functions for arithmetic tasks.
- `data_utils.py` employs pandas for clear demonstrations of data handling capabilities.

## Contributing
Contributions in the form of issues or pull requests are welcome to improve this toolset or to add features.

## License
This project is licensed under the MIT License.

## Contact
For any questions, please reach out via email at `your-email@example.com`.