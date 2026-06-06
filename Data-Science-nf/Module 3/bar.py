#Bar Chart (Double bar)

import matplotlib.pyplot as plt

subject = ["Python", "JavaScript", "React.js", "TypeScript"]
score1 = [50, 60, 70, 80]
score2 = [55, 65, 75, 85]

# positions 
x = list(range(len(subject)))
width = 0.35

# bars
plt.bar([i - width/2 for i in x], score1, width, label="Exam 1", color="green")
plt.bar([i + width/2 for i in x], score2, width, label="Exam 2", color="blue")

# labels
plt.xlabel("Subjects")
plt.ylabel("Score")
plt.title("Double Bar Chart")

# grid
plt.grid(axis="y", linestyle="--", linewidth=1, color="gray", alpha=0.5)

# x-axis labels
plt.xticks(x, subject)

# values on bars
for i in x:
    plt.text(i - width/2, score1[i] + 1, str(score1[i]), ha="center")
    plt.text(i + width/2, score2[i] + 1, str(score2[i]), ha="center")

# legend
plt.legend()

plt.show()