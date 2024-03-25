import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
tips = sns.load_dataset("tips")

# Create a boxplot of total bills by day
sns.boxplot(x="day", y="total_bill", data=tips)

# Show the plot
plt.show()