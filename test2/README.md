# Project Title: DataFrame Operations Utility

## Overview

This project demonstrates basic operations on a `pandas` DataFrame using Python. The primary focus is on showcasing how data can be managed, manipulated, and analyzed with simple yet powerful scripts. These operations involve creating a DataFrame, performing calculations, and enhancing data with new columns.

## File Descriptions

### **File Name: `utils.py`**

- **Purpose**: 
  This script creates a sample DataFrame and performs basic operations to demonstrate data analysis using `pandas`.

- **Functions and Features**:
  - **DataFrame Creation**: Constructs a DataFrame with names, ages, and cities.
  - **Display**: Prints the DataFrame to the console.
  - **Mean Age Calculation**: Computes and prints the mean age from the DataFrame.
  - **Filtering**: Extracts and displays rows where the age is greater than 25.
  - **New Column Addition**: Adds a column named "Age in 5 Years," which shows projected ages.

- **Dependencies**: 
  - `pandas`: Ensure you have the `pandas` library installed. You can find more information [here](https://pandas.pydata.org/pandas-docs/stable/).

## Setup Instructions

1. **Prerequisites**: Ensure Python is installed on your system. You can download it [here](https://www.python.org/downloads/).

2. **Install Dependencies**:
   ```bash
   pip install pandas
   ```
   
3. **Download the Script**: Clone or download the `utils.py` file from the repository.

## Usage Guide

To run the script, execute the following command in your terminal:

```bash
python utils.py
```

### Example Output

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

Currently, this project consists only of a single script file, `utils.py`, which is standalone and does not interact with other files.

## Contributing

We welcome contributions! Please fork the repository and submit a pull request with a detailed description of changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or suggestions, please contact [your-email@example.com].