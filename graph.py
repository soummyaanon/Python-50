import matplotlib.pyplot as plt
import numpy as np


plt.figure(figsize=(10, 10))

# Pie chart
runs = np.array([350,250,255,150])
players = ["Dhoni"," Kholi","Pandya","Gill"]
plt.subplot(221)  
plt.pie(runs, labels=players)

# Bar chart
overs = np.array(["1","2","3","4","5","6","7","8","9","10"])
runs=np.array([3,8,1,10,5,7,8,9,6,5])
plt.subplot(222)  
plt.bar(overs,runs)

# Line plot
overs=[10,20,30,40,50]
runs=[12,4,14,7,9]
plt.subplot(223)  
plt.plot(overs,runs)

# Scatter plot
player=np.array([10,4,5,7,1])
average=np.array([42,68,56,40,69])
plt.subplot(224)  
plt.scatter(player,average)

plt.tight_layout()
plt.show()