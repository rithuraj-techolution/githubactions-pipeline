# Project Title: Techolution Data and Utility Toolkit

## Overview
The Techolution Data and Utility Toolkit is a comprehensive project designed to provide basic mathematical utilities and data management features for Python developers. It includes standalone Python scripts for performing arithmetic operations, manipulating data using a DataFrame, and a `main.py` script demonstrating colored text output.

## File Descriptions

### File Name: `main.py`
- **Purpose**: Demonstrates colorful text output using the `colorama` library.
- **Functions and Features**:
  - **Color Printing**: Uses `colorama` to print "Hello World" in red.
  - **Dependencies**: Requires `colorama`.
- **Dependencies**:
  - `colorama`: Install via `pip install colorama`.

### File Name: `utils.py`
- **Purpose**: Provides basic arithmetic functions.
- **Functions and Features**:
  - **`add(a, b)`**: Returns the sum of `a` and `b`.
  - **`subtract(a, b)`**: Returns the difference between `a` and `b`.
  - **`multiply(a, b)`**: Returns the product of `a` and `b`.
  - **`divide(a, b)`**: Divides `a` by `b`, raises `ValueError` if `b` is zero.

### Data Management Features in `utils.py`
- **Purpose**: Demonstrates simple data manipulations using a DataFrame.
- **Functions and Features**:
  - **Create DataFrame**: Initializes a DataFrame with sample data.
  - **Calculate Mean**: Computes mean of the 'Age' column.
  - **Filter Data**: Filters rows where age is greater than 25.
  - **Add Column**: Adds a new 'Age in 5 Years' column.
- **Dependencies**:
  - `pandas`: Install via `pip install pandas`.

## Setup Instructions
1. **Clone Repository**: `git clone https://github.com/rithuraj-techolution/githubactions-pipeline.git`
2. **Install Dependencies**:
   ```bash
   pip install colorama pandas
   ```

## Usage Guide
- **Running `main.py`**: Execute `python main.py` to see text printed in red.
- **Running `utils.py`**: 
  - Calculation functions: Call directly in a Python interpreter.
  - Data operations: Run `python utils.py` to display DataFrame examples.

## Examples
### Example 1: Arithmetic with `utils.py`
```python
from utils import add, divide
result = add(5, 7)        # Output: 12
quotient = divide(10, 2)  # Output: 5.0
```

### Example 2: DataFrame Operations
```shell
python utils.py
```

## How the Files Relate
- `main.py` provides an example of console output customization which can be used in conjunction with results from `utils.py`.
- Arithmetic functions in `utils.py` can process numerical data before integration into larger data structures such as DataFrames.

## Contributing
- **Add New Files**: Fork the repository, create a feature branch, commit changes, and open a pull request.
- **Enhance Existing Files**: Follow existing code style; ensure any new functions have accompanying test cases.

## License
- Distributed under the MIT License.

## Contact
- Maintained by Rithuraj Techolution. For queries or contributions, reach out at [rithuraj.nambiar@techolution.com](mailto:rithuraj.nambiar@techolution.com).
