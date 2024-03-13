import pandas as pd 

data = ({"Name": ["John", "Anna", "Peter", "Linda"],
         "Location": ["New York", "Paris", "Berlin", "London"],
         "Age": [24, 13, 53, 33]})
df = pd.DataFrame(data)
pivot = df.pivot(index="Name", columns="Location", values="Age")
print(pivot)