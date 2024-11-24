# Project Title: GitHub Actions Pipeline

## Overview
The GitHub Actions Pipeline project is designed to automate workflows such as testing, building, and deployment in code repositories. This project contains standalone scripts and configuration files that facilitate various tasks, ranging from printing colored text in the terminal to executing workflows triggered by pull requests and manual triggers.

## File Descriptions

### File: `main.py`
- **Purpose**: Prints "Hello World" in red text using `colorama`.
- **Functions and Features**:
  - Utilizes `colorama` to change text color.
  - Direct terminal print with color reset.
  - **Dependencies**: Requires the `colorama` library.
- **Example Usage**:
  ```bash
  python main.py
  ```

### File: `utils.py`
- **Purpose**: Provides basic arithmetic functions and data manipulation in a pandas DataFrame.
- **Functions and Features**:
  - **Arithmetic Functions**:
    - `add(a, b)`: Returns the sum.
    - `subtract(a, b)`: Returns the difference.
    - `multiply(a, b)`: Returns the product.
    - `divide(a, b)`: Returns the quotient; raises error if `b` is 0.
  - **DataFrame Manipulations**:
    - Creates a sample DataFrame with names, ages, and cities.
    - Calculates mean age and filters age > 25.
    - Adds a new column for age in 5 years.
  - **Dependencies**: Requires `pandas` library.
- **Example Usage**:
  ```python
  from utils import add, subtract
  print(add(5, 3))
  ```

### File: `pr-refactor.yml`
- **Purpose**: Executes workflows on pull request events and manual triggers.
- **Functions and Features**:
  - Automates data fetching and API communication for pull requests.
  - Jobs for PR and manual events with conditionals.
- **Dependencies**: `github` actions, token access configured in GitHub secrets.

## Setup Instructions
1. Clone the repository: `git clone https://github.com/rithuraj-techolution/githubactions-pipeline.git`.
2. Navigate to project directory.
3. Install dependencies:
   ```bash
   pip install colorama pandas
   ```

## Usage Guide
- Run `main.py` with: `python main.py`.
- Use functions in `utils.py` directly in the Python interpreter or script by importing.

## Examples
- Running `main.py`:
  ```bash
  $ python main.py
  Hello World   # Display in red.
  ```
- Utilizing `utils.py` arithmetic functions:
  ```python
  from utils import add
  print(add(2, 3)) # Output: 5
  ```

## How the Files Relate
- `main.py` is independent print-focused utility.
- `utils.py` is a versatile utility script that can be incorporated into other Python applications requiring basic operations.
- `pr-refactor.yml` automates workflow processes, utilizing GitHub events and API to streamline project updates and triggers.

## Contributing
- Fork the repository and create your branch (`git checkout -b feature/YourFeature`).
- Commit changes (`git commit -am 'Add new feature'`).
- Push to the branch (`git push origin feature/YourFeature`).
- Open a pull request.

## License
This project is licensed under the MIT License.

## Contact
For questions or contributions, contact Rithuraj Nambiar at [rithuraj.nambiar@techolution.com](mailto:rithuraj.nambiar@techolution.com).