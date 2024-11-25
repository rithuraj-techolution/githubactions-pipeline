 
import pandas as pd

def create_sample_dataframe():
    """Create and return a sample DataFrame."""
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [24, 27, 22, 32],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
    }
    return pd.DataFrame(data)

def display_dataframe(df, title):
    """Display the DataFrame with a given title."""
    print(f"\n{title}:")
    print(df)

def calculate_mean_age(df):
    """Calculate and print the mean age from the DataFrame."""
    mean_age = df['Age'].mean()
    print("\nMean Age:", mean_age)
    return mean_age

def filter_dataframe_by_age(df, age_threshold):
    """Return a filtered DataFrame with rows where age is greater than a given threshold."""
    return df[df['Age'] > age_threshold]

def add_age_in_5_years_column(df):
    """Add a new column 'Age in 5 Years' to the DataFrame."""
    df['Age in 5 Years'] = df['Age'] + 5

def main():
    # Create a sample DataFrame
    df = create_sample_dataframe()
    
    # Display the original DataFrame
    display_dataframe(df, "Sample DataFrame")
    
    # Perform some basic operations
    # Calculate the mean age
    calculate_mean_age(df)
    
    # Filter rows where age is greater than 25 and display
    filtered_df = filter_dataframe_by_age(df, 25)
    display_dataframe(filtered_df, "Filtered DataFrame (Age > 25)")
    
    # Add a new column and display the modified DataFrame
    add_age_in_5_years_column(df)
    display_dataframe(df, "DataFrame with new column 'Age in 5 Years'")

if __name__ == "__main__":
    main()
