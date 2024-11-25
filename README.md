# Project Title: Python Utility Toolset

## Overview
This project is a simple utility toolset providing basic arithmetic operations, data manipulation with pandas, and colorized console output. It demonstrates how to combine core Python functionalities with third-party libraries to enhance console applications.

## File Descriptions

### 1. `main.py`
- **Purpose**: Demonstrates basic console output with enhanced visuals.
- **Functions and Features**: 
  - Uses the `colorama` library to print "Hello World" in red text.
- **Dependencies**: 
  - `colorama` - A library to produce colored terminal text. 
  - **Installation**: `pip install colorama`

### 2. `utils.py`
- **Purpose**: Performs basic arithmetic operations.
- **Functions and Features**:
  - `add(a, b)`: Returns the sum of `a` and `b`.
  - `subtract(a, b)`: Returns the difference of `a` and `b`.
  - `multiply(a, b)`: Returns the product of `a` and `b`.
  - `divide(a, b)`: Returns the division of `a` by `b` and raises an error if `b` is zero.
- **Dependencies**: None

### 3. `data_utils.py`
- **Purpose**: Demonstrates basic data manipulation using pandas.
- **Functions and Features**:
  - Creates a DataFrame with sample data.
  - Calculates the mean age, filters data based on age, and adds a column for age in 5 years.
- **Dependencies**: 
  - `pandas` - A powerful data analysis and manipulation library.
  - **Installation**: `pip install pandas`

## Setup Instructions
1. Clone the repository to your local machine.
2. Install required dependencies using the command:
   ```bash
   pip install colorama pandas
   ```

## Usage Guide

### Running Files
- **`main.py`**: 
  ```bash
  python main.py
  ```
  - **Output**: Displays "Hello World" in red.

- **Utility Operations (`utils.py`)**:
  - Import `utils.py` in your script and call functions like:
    ```python
    from utils import add, subtract, multiply, divide

    print(add(5, 3))         # Output: 8
    print(subtract(5, 3))    # Output: 2
    ```

- **Data Operations (`data_utils.py`)**:
  ```bash
  python data_utils.py
  ```
  - **Output**: Displays the sample DataFrame, mean age, filtered data, and updates to the DataFrame.

## How the Files Relate
- `main.py` demonstrates integration with external libraries for styling console output.
- `utils.py` provides basic arithmetic functions that can be included in other Python scripts.
- `data_utils.py` uses pandas for data handling, showing how data manipulation can be performed efficiently.

## Contributing
Feel free to open issues or submit pull requests to enhance functionality or add new features.

## License
This project is licensed under the MIT License.

## Contact
For questions, feel free to reach out via email at `your-email@example.com`.