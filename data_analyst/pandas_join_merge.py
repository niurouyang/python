# how pandas join and merge function works
import pandas as pd

# Create two DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3]}, index=['a', 'b', 'c'])
df2 = pd.DataFrame({'B': [4, 5, 6]}, index=['b', 'c', 'd'])

# Joining using the join() method
result = df1.join(df2, how='outer')  # 'inner' is the default join type

print(result)

# Create two DataFrames
df1 = pd.DataFrame({'key': ['a', 'b', 'c'], 'value1': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['b', 'c', 'd'], 'value2': [4, 5, 6]})

print(df1)
print(df2)

# Merging using the merge() function
result = pd.merge(df1, df2, on='key', how='inner')

print(result)