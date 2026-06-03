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

# Y-axis labels: 0,10,20,...,100
plt.yticks(range(0, 101, 10))

# Grid style
plt.grid(True, linestyle='--', linewidth=1,color="blue")

# Legend
plt.legend()

# Show graph
plt.show()