# Python Project

## Overview
This project consists of several standalone Python scripts designed to perform different tasks, such as data manipulation using Pandas, simple arithmetic operations, and color-coded printing in the console. These scripts can be used independently or integrated as needed for larger projects.

## File Descriptions

### 1. main.py
- **Purpose**: Prints a "Hello World" message in red.
- **Functions and Features**:
  - Uses `colorama` to display text in color.
- **Dependencies**: Requires `colorama` library.
- **Example Usage**:
  ```python
  # Colorful "Hello World"
  python main.py
  ```

### 2. utils.py
#### Version 1
- **Purpose**: A collection of basic arithmetic functions.
- **Functions and Features**:
  - `add(a, b)`: Returns the sum of two numbers.
  - `subtract(a, b)`: Returns the difference.
  - `multiply(a, b)`: Returns the product.
  - `divide(a, b)`: Returns the quotient; handles division by zero.

#### Version 2
- **Purpose**: Demonstrates data manipulation using Pandas.
- **Functions and Features**:
  - Creates and displays a sample DataFrame.
  - Calculates mean age.
  - Filters DataFrame by age.
  - Adds a new column with age incremented by 5.
- **Dependencies**: Requires `pandas` library.
- **Example Usage**:
  ```python
  # Data manipulation with Pandas
  python utils.py
  ```

### 3. pr-refactor.yml
- **Purpose**: GitHub Action for processing pull requests and manual triggers.
- **Functions and Features**:
  - Automates data fetching from GitHub and sends to an API.
  - Supports both pull request events and manual executions.
- **Dependencies**: Utilizes GitHub secrets and `jq` for JSON processing.

## Setup Instructions
1. **Install Dependencies**:
   ```bash
   pip install colorama pandas
   ```

## Usage Guide
- For `main.py`: Run the script directly with Python to see the colored output.
- For `utils.py` (both versions), ensure the necessary data manipulation libraries are installed.

## Examples
- To see the colorful "Hello World", use:
  ```bash
  python main.py
  ```
- For data operations:
  ```bash
  python utils.py
  ```

## How the Files Relate
- `main.py` and `utils.py` can be used independently or together for a project needing console output and data handling.

## Contributing
1. Fork the repository.
2. Create a new branch for your feature.
3. Ensure code is well-documented and tested.
4. Create a pull request with detailed description.

## License
This project is licensed under the MIT License.

## Contact
For questions or contributions, reach out to Rithuraj Techolution at rithuraj.nambiar@techolution.com.