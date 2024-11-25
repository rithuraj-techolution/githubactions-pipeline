# Project Title: DataFrame Operations with Pandas

## Overview
This project demonstrates basic operations using the pandas library to manipulate and analyze tabular data within a DataFrame. The script `utils.py` creates a sample DataFrame and performs various operations such as calculating the mean age, filtering data, and adding new columns to enhance data analysis capabilities.

## File Descriptions

### utils.py

- **Purpose**: 
  This script is designed to showcase how to effectively use pandas for data manipulation, focusing on basic but essential operations on a DataFrame.

- **Functions and Features**:
  - **Sample DataFrame Creation**: Initializes a DataFrame with sample data including names, ages, and cities.
  - **Mean Age Calculation**: Computes the average age of individuals in the DataFrame.
  - **Data Filtering**: Extracts rows where the age is greater than 25.
  - **Column Addition**: Introduces a new column, `Age in 5 Years`, to project age advancement.

- **Dependencies**:
  - Requires the pandas library. Ensure it is installed using pip:
    ```shell
    pip install pandas
    ```

## Setup Instructions
1. Ensure Python is installed on your machine. You can download it from [python.org](https://www.python.org/).
2. Install pandas using:
   ```shell
   pip install pandas
   ```
3. Save the `utils.py` script to your preferred directory.

## Usage Guide
To execute the script and observe the output of the DataFrame operations:
1. Open your terminal.
2. Navigate to the directory containing `utils.py`.
3. Run the script using:
   ```shell
   python utils.py
   ```

## Examples
Upon running the script, you should see outputs like the following:
- The initial DataFrame display showcasing names, ages, and cities.
- The mean age of the individuals.
- A filtered DataFrame where all individuals are older than 25.
- A modified DataFrame with an additional column reflecting each person’s age in five years.

## How the Files Relate
Currently, the project consists of a single script that independently performs a series of operations on a DataFrame to demonstrate various functionalities of the pandas library.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with a detailed description of any enhancements or additional features you have added.

## License
This project is licensed under the MIT License.

## Contact
For questions or suggestions, please contact [youremail@example.com](mailto:youremail@example.com).