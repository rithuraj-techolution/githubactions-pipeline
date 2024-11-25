# Project Title
Simple Python Operations and Data Management

## Overview
This project encompasses a collection of Python scripts designed to perform basic arithmetic operations and manage data using `pandas`. The main focus is on demonstrating simple console output with color and basic data manipulation techniques.

## File Descriptions

### `main.py`
- **Purpose**: Print a "Hello World" message in red text to the console using the `colorama` module.
- **Functions and Features**:
  - Utilizes `colorama.Fore` for colored text output in terminal/console. The code uses `Fore.RED` to make the text red.
- **Dependencies**:
  - `colorama`: For colored console output.
  - Install using: `pip install colorama`.

### `utils.py`
- **Purpose**: Perform basic arithmetic operations.
- **Functions and Features**:
  - `add(a, b)`: Returns the sum of `a` and `b`.
  - `subtract(a, b)`: Returns the difference between `a` and `b`.
  - `multiply(a, b)`: Returns the product of `a` and `b`.
  - `divide(a, b)`: Returns the quotient of `a` divided by `b`. Raises `ValueError` if `b` is zero.
- **Dependencies**: None

### `data_operations.py`
(Note: The description provided seems intended for `utils.py`, but here it’s described separately for clarity)
- **Purpose**: Manage and perform operations on a sample dataframe using `pandas`.
- **Functions and Features**:
  - Creates a sample DataFrame with columns `Name`, `Age`, and `City`.
  - Calculates and prints the mean age.
  - Filters and prints rows where `Age` is greater than 25.
  - Adds a new column `Age in 5 Years` and prints the updated DataFrame.
- **Dependencies**:
  - `pandas`: For data manipulation and analysis.
  - Install using: `pip install pandas`.

## Setup Instructions
1. **Clone the Repository**: 
   ```bash
   git clone <repository-url>
   ```
2. **Install Dependencies**:
   ```bash
   pip install colorama pandas
   ```

## Usage Guide

### Running `main.py`
```bash
python main.py
```
**Output**: Displays "Hello World" in red text.

### Using `utils.py`
- Import functions into your script:
  ```python
  from utils import add, subtract, multiply, divide
  
  print(add(5, 3))  # Example usage
  ```

### Running `data_operations.py`
```bash
python data_operations.py
```
**Output**: Displays the sample DataFrame, mean age, filtered rows, and DataFrame with an additional column.

## Examples
- **main.py**: Outputs a red "Hello World".
- **utils.py**: 
  ```python
  print(add(10, 5))  # Output: 15
  print(divide(10, 2))  # Output: 5.0
  ```
- **data_operations.py**: 
  ```bash
  Sample DataFrame:
    Name  Age         City
  0  Alice   24     New York
  1    Bob   27  Los Angeles
  2 Charlie   22      Chicago
  3  David   32      Houston
  ```

## How the Files Relate
- `main.py` is independent and demonstrates the usage of `colorama`.
- `utils.py` contains functions that can be reused across other Python scripts.
- `data_operations.py` showcases how to manipulate data using `pandas`.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License
This project is licensed under the MIT License.

## Contact
For questions or contributions, please contact [your-email@example.com].