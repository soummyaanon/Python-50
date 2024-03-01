import pandas as pd

mca1 = pd.DataFrame({
    'Name': ['A', 'B', 'C', 'D'],
    'Age': [20, 21, 19, 18],
    'adress': ['Pune', 'Mumbai', 'Nagpur', 'Nashik'],
    'marks': [80, 85, 90, 95]
}, index=[1, 2, 3, 4])

mca2 = pd.DataFrame({
    'Name': ['E', 'F', 'G', 'H'],
    'Age': [20, 21, 19, 18],
    'adress': ['Pune', 'Mumbai', 'Nagpur', 'Nashik'],
    'marks': [80, 85, 90, 95]
}, index=[5, 6, 7, 8])

mca3 = pd.DataFrame({
    'Name': ['I', 'J', 'K', 'L'],
    'Age': [20, 21, 19, 18],
    'adress': ['Pune', 'Mumbai', 'Nagpur', 'Nashik'],
    'marks': [80, 85, 90, 95]
}, index=[9, 10, 11, 12])

merged = pd.concat([mca1, mca2, mca3])

print(merged)