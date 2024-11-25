# Project Title: Basic Python Utilities and Data Manipulation

## Overview
This project provides a set of Python scripts for basic operations and data manipulation. It includes functionalities for mathematical computations and handling DataFrames using `pandas`.

## File Descriptions

### `main.py`
- **Purpose**: Demonstrates simple console output using color formatting.
- **Functions and Features**: 
  - Uses the `colorama` library to print "Hello World" in red.
- **Dependencies**: 
  - `colorama` (install via `pip install colorama`)

### `utils.py`
- **Purpose**: Offers basic arithmetic operations useful for general-purpose calculations.
- **Functions and Features**:
  - `add(a, b)`: Returns the sum of two numbers.
  - `subtract(a, b)`: Returns the difference between two numbers.
  - `multiply(a, b)`: Returns the product of two numbers.
  - `divide(a, b)`: Returns the quotient of two numbers. Raises an error if the second number is zero.

### `data_utils.py`
- **Purpose**: Demonstrates simple data manipulation techniques using pandas.
- **Functions and Features**:
  - Creates a sample DataFrame with names, ages, and cities.
  - Calculates the mean age.
  - Filters rows where age is greater than 25.
  - Adds a new column for projected age in 5 years.
- **Dependencies**:
  - `pandas` (install via `pip install pandas`)

## Setup Instructions
1. Install required packages:
   ```bash
   pip install colorama pandas
   ```

## Usage Guide

### Running `main.py`
Execute the script to see colored console output:
```bash
python main.py
```
Expected output:
```
Hello World
```
(in red)

### Running `data_utils.py`
Execute the script to perform data manipulation:
```bash
python data_utils.py
```
Expected output:
```
Sample DataFrame:
      Name  Age         City
0    Alice   24     New York
1      Bob   27  Los Angeles
2  Charlie   22      Chicago
3    David   32      Houston

Mean Age: 26.25

Filtered DataFrame (Age > 25):
   Name  Age         City
1   Bob   27  Los Angeles
3 David   32      Houston

DataFrame with new column 'Age in 5 Years':
      Name  Age         City  Age in 5 Years
0    Alice   24     New York             29
1      Bob   27  Los Angeles             32
2  Charlie   22      Chicago             27
3    David   32      Houston             37
```

## How the Files Relate
- `main.py` is an independent script for demonstrating console output formatting.
- `utils.py` provides arithmetic functions that could be utilized in other scripts for calculations.
- `data_utils.py` focuses on data manipulation and operates independently from the other scripts.

## Contributing
Feel free to contribute by submitting pull requests or opening issues to suggest improvements.

## License
This project is licensed under the MIT License.

## Contact
For further questions or contributions, please reach out via GitHub issues.