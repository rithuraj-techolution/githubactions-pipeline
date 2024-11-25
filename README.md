# Project Title: Python Utilities and DataFrame Operations

## Overview
This project contains Python scripts that demonstrate basic text styling, arithmetic operations, and data manipulation using DataFrames. `main.py` introduces color to console outputs, while `utils.py` offers basic arithmetic functions and DataFrame operations common in data analysis tasks.

## File Descriptions

### File: `main.py`
- **Purpose:** Outputs a stylized "Hello World" message to the console.
- **Functions and Features:**
  - Utilizes `colorama` for color styling console outputs.
  - Changes text color to red and then resets it.
- **Dependencies:** 
  - Requires the `colorama` library. Install via `pip install colorama`.

### File: `utils.py`
- **Purpose:** Contains utility functions and DataFrame operations.
- **Functions and Features:**
  - **Arithmetic Functions**:
    - `add(a, b)`: Returns the sum of `a` and `b`.
    - `subtract(a, b)`: Returns the difference between `a` and `b`.
    - `multiply(a, b)`: Returns the product of `a` and `b`.
    - `divide(a, b)`: Returns the division of `a` by `b`; raises an error if `b` is zero.
  - **DataFrame Operations**:
    - Creates a sample DataFrame with names, ages, and cities.
    - Calculates the mean age.
    - Filters DataFrame rows where age is greater than 25.
    - Adds a new column `Age in 5 Years` showing future ages.
- **Dependencies:**
  - Requires the `pandas` library. Install via `pip install pandas`.

## Setup Instructions
1. Ensure Python is installed on your system.
2. Install necessary dependencies with:
   ```bash
   pip install colorama pandas
   ```

## Usage Guide
- To run the `main.py` file:
  ```bash
  python main.py
  ```
  This prints "Hello World" in red.
  
- To execute functions in `utils.py`, import the script in your Python environment or run directly with:
  ```bash
  python utils.py
  ```
  This demonstrates DataFrame operations and prints results to the console.

## Examples
- **Example for Arithmetic Functions in `utils.py`:**
  ```python
  from utils import add, subtract

  print(add(5, 3))  # Output: 8
  print(subtract(5, 3))  # Output: 2
  ```

- **Example for DataFrame Operations:**
  Running `utils.py` will display various DataFrame manipulations, such as mean age calculation and filtered datasets.

## How the Files Relate
Both files function independently. `main.py` focuses on stylized output, while `utils.py` concentrates on numeric and DataFrame operations, showcasing Python’s versatility in handling different tasks.

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests. Ensure to follow standard coding practices and include tests where applicable.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Contact
For questions or contributions, reach out via GitHub issues or contact the maintainer via email: [your-email@example.com].