import pandas as pd
from matplotlib.pyplot import pie, axis, show

import matplotlib.pyplot as plt

df = pd.read_csv("/Users/soumyaram/Python-50/Doc.csv")
sums = df.groupby(df["Name"])["Marks"].sum()

# Plot the pie chart with percentage values
pie(sums, labels=sums.index, autopct='%1.1f%%')

show()
