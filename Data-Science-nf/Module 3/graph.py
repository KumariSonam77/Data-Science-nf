#define dataset with dictionary

import pandas as pd
import matplotlib.pyplot as plt

# Theme
plt.style.use('ggplot')

# Dataset
marks = {"marks": [20, 30, 40, 50, 60]}
var = pd.DataFrame(marks)

# Figure size
plt.figure(figsize=(5, 3))

# Get current axes
ax = plt.gca()
ax.set_facecolor("orange")

# Plot color and style
plt.plot(var["marks"],marker='o',markerfacecolor='yellow',markeredgecolor='black',linestyle='--',linewidth=5,color='red',label='Marks')

# Labels
plt.xlabel("Student Number", fontsize=12, color="yellow")
plt.ylabel("Marks", fontsize=12, color="green")

# Title
plt.title("Student Marks", fontsize=14, color="purple")

# Limits
plt.ylim(0, 100)
plt.xlim(0, 10)

# Ticks (positions + labels)
plt.xticks(range(0, 11, 1),["0","1","2","3","4","5","6","7","8","9","10"])
plt.yticks(range(0, 101, 10),["0","10","20","30","40","50","60","70","80","90","100"])

# Spin effect (rotate labels)
plt.xticks(rotation=45)   

# Grid style
plt.grid(True, linestyle='--', linewidth=1,color="blue")

# Annontations
plt.annotate("Low Score",xy=(0, 20),xytext=(1, 35),arrowprops=dict(color='black',linewidth=3, arrowstyle="->"))
plt.annotate("Good Score",xy=(4, 60),xytext=(3, 75),arrowprops=dict(color='black',linewidth=3, arrowstyle="->"))

# Legend
plt.legend()

# Show graph
plt.show()