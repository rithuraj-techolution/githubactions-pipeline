import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}


df = pd.DataFrame(data)

# Display the DataFrame
print("Sample DataFrame:")
print(df)

# Perform some basic operations
# Calculate the mean age
mean_age = df['Age'].mean()
print("\nMean Age:", mean_age)

# Filter rows where age is greater than 25
filtered_df = df[df['Age'] > 25]
print("\nFiltered DataFrame (Age > 25):")
print(filtered_df)

# Add a new column
df['Age in 5 Years'] = df['Age'] + 5
print("\nDataFrame with new column 'Age in 5 Years':")
print(df)
