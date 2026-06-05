#median line (Histogram)
import matplotlib.pyplot as plt
marks = [50, 56, 72, 88, 98, 60, 62, 74, 92, 90]

# Step 1: Sort data
sorted_marks = sorted(marks)

# Step 2: Calculate median manually
n = len(sorted_marks)
if n % 2 == 0:
    median_value = (sorted_marks[n//2 - 1] + sorted_marks[n//2]) / 2
else:
    median_value = sorted_marks[n//2]

# Figure
plt.figure(figsize=(5, 3))

# Histogram
plt.hist(marks, bins=4, edgecolor="red", color="purple", alpha=0.5)

# Median line
plt.axvline(median_value, color="green", linestyle="--", linewidth=2)

# Show median value on graph
plt.text(median_value + 1, 2, f"Median = {median_value}",  color="green", fontsize=10)

# Title and labels
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")

# Grid
plt.grid(axis="y", linestyle='--', linewidth=1, color="blue")

plt.show()