#dobble bar chart
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Exam1": [50, 60, 70, 80],
    "Exam2": [55, 65, 75, 85]
}, index=["Python", "JavaScript", "React.js", "TypeScript"])

df.plot(kind="bar", figsize=(7,5))

plt.title("Double Bar Chart")
plt.ylabel("Scores")
plt.xlabel("Subjects")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.show()