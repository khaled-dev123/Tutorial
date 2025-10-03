import pandas as pd

# 1. DataFrame Creation & Construction
# Make a DataFrame from a two-dimensional list.
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
df = pd.DataFrame(data, columns=['A', 'B', 'C'])
print("DataFrame from 2D list:\n", df)

# Create a DataFrame from a dict of lists/arrays.
data_dict = {'A': [1, 4, 7], 'B': [2, 5, 8], 'C': [3, 6, 9]}
df_dict = pd.DataFrame(data_dict)
print("\nDataFrame from dict of lists:\n", df_dict)

# Create a DataFrame from a list of dicts.
data_list_of_dicts = [{'A': 1, 'B': 2}, {'A': 4, 'B': 5, 'C': 6}, {'A': 7, 'C': 9}]
df_list_of_dicts = pd.DataFrame(data_list_of_dicts)
print("\nDataFrame from list of dicts:\n", df_list_of_dicts)

# Construct a DataFrame from list of tuples.
data_tuples = [(1, 2), (3, 4), (5, 6)]
df_tuples = pd.DataFrame(data_tuples, columns=['A', 'B'])
print("\nDataFrame from list of tuples:\n", df_tuples)

# Convert list of nested dictionaries into a DataFrame.
data_nested_dicts = [{'A': {'a': 1, 'b': 2}}, {'A': {'a': 3, 'b': 4}}, {'A': {'a': 5, 'b': 6}}]
df_nested_dicts = pd.json_normalize(data_nested_dicts)
print("\nDataFrame from nested dicts:\n", df_nested_dicts)

# Create a DataFrame from Pandas Series.
data_series = {'A': pd.Series([1, 2, 3]), 'B': pd.Series([4, 5, 6])}
df_series = pd.DataFrame(data_series)
print("\nDataFrame from Pandas Series:\n", df_series)

# Construct a DataFrame from string data and clean string values.
data_string = {'A': ['  foo ', ' bar', 'baz  '], 'B': ['  one', 'two ', ' three ']}
df_string = pd.DataFrame(data_string)
df_string = df_string.applymap(lambda x: x.strip())
print("\nDataFrame from string data (cleaned):\n", df_string)

# These cover almost all possible ways to create a DataFrame.
df.info()

# 2. DataFrame Indexing & Reindexing

# Reindexing in Pandas DataFrame.
# Reset Index in Pandas DataFrame.
# Change column names and row indexes.
# Mapping external values to DataFrame values.
# Reshape DataFrame using stack, unstack, and melt.
# Mastering these ensures you can organize, reshape, and map your data effectively.

# 3. DataFrame Row Operations
# Select rows based on conditions.
# Use iloc[] and iat[] for row selection.
# Drop rows based on a condition.
# Insert a row at a given position.
# Iterate over rows in multiple ways.
# Select row with maximum/minimum value.
# Randomly select rows from the DataFrame.
# These exercises cover almost all row-level manipulations you will need.

# 4. DataFrame Column Operations
# Create new columns (from existing columns, loops, or conditions).
# Rename columns and lowercase/uppercase/capitalize column names.
# Get unique values from a column.
# Conditional operations on columns.
# Split a column into multiple columns using regex or string methods.
# Column arithmetic: difference, sum, or derived calculations.
# Get n-largest/n-smallest values from a column.
# Drop columns effectively.
# Frequency counts of column values.
# Change data types for columns.
# Column manipulation is one of the most used skills in real-world Pandas tasks.

# 5. DataFrame Cleaning
# Remove or fill empty cells (dropna, fillna).
# Fix wrong data formats (astype).
# Fix wrong data using apply() and conditions.
# Remove duplicates (drop_duplicates).
# Clean string columns using regex, str.replace, str.strip, etc.
# This ensures your datasets are analysis-ready.

# 6. Pandas Series
# Create a Series from arrays, lists, or dictionaries.
# Create a Series using NumPy functions.
# Access elements by index, label, or slicing.
# Perform vectorized operations on a Series.
# Mastering Series helps you work with single columns efficiently.

# 7. Pandas Date & Time
# Convert string columns to datetime (pd.to_datetime).
# Work with Timedelta and Period for date/time calculations.
# Manipulate time-series indexes for analysis.
# Date and time operations are critical for finance, analytics, and sensor data.

# 8. Analyzing DataFrames
# Use head() and tail() to preview data.
# Use info() to check data types and null values.
# Use describe() for quick statistics.
# Count null values per column (isnull().sum()).
# Get row/column summaries using sum(), mean(), value_counts().
# These exercises make you confident in exploratory data analysis (EDA).
