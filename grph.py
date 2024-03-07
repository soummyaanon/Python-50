import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import pie, axis, show
df = pd.read_csv("/Users/soumyaram/Python-50/Doc.csv")
sums = df.groupby(df["Name"])["Marks"].sum()
pie(sums, labels=sums.index);
show()

