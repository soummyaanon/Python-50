import pandas as pd
import numpy as np

# 1) Create a dataset using numpy
data = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12],
                 [13, 14, 15, 16],
                 [17, 18, 19, 20]])

# Convert the numpy array to a pandas DataFrame
df = pd.DataFrame(data, columns=['Column1', 'Column2', 'Column3', 'Column4'])

# 2) Cleaning the Data
# For demonstration, let's replace all values of 5 with NaN
df = df.replace(5, np.nan)

# Use fillna to replace NaN values with a specific value, such as 0
df = df.fillna(0)
# Use dropna to remove rows with NaN values
df = df.dropna()

# Use fillna to replace NaN values with a specific value, such as 0
df = df.fillna(0)
# 3) Data frame manipulation
# Add a new column to the DataFrame with values generated by numpy
df['Column5'] = np.arange(len(df))

# Print the DataFrame
print(df)