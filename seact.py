from matplotlib import pyplot as plt
import seaborn as sns

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a line plot using Seaborn
sns.lineplot(x=x, y=y, marker='o', linestyle='--', color='blue')  # Customize marker, linestyle, and color

plt.show()