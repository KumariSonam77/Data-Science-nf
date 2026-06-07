#This code visualizes monthly sales and revenue data using different charts to analyze trends, comparison, distribution, and relationships.

import matplotlib.pyplot as plt

info = {
    "months": ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
    "unit": [10, 15, 18, 16, 11, 20, 14, 17, 19, 13, 12, 22],
    "revenue": [100, 150, 800, 300, 500, 600, 450, 700, 650, 400, 350, 900]
}

# 1. LINE CHART 
plt.figure(figsize=(10,5))
plt.plot(info["months"], info["unit"], marker='o', color='blue', linestyle='--')

plt.xlabel("Months", fontsize=12, color="purple")
plt.ylabel("Unit", fontsize=12, color="purple")
plt.title("Monthly Unit Trend", fontsize=14)

plt.xticks(rotation=45)
plt.grid()
plt.show()

# 2. BAR CHART 
plt.figure(figsize=(6,3))
plt.bar(info["months"], info["unit"], color=["blue","black","yellow","purple","gray","orange"])

plt.title("Monthly Unit Comparison")
plt.xlabel("Months")
plt.ylabel("Unit")
plt.xticks(rotation=45)
plt.show()

# 3. HISTOGRAM 
plt.figure(figsize=(6,3))
plt.hist(info["unit"], bins=4, color='green', edgecolor='black', alpha=0.5)

plt.title("Distribution of Units")
plt.xlabel("Unit Range")
plt.ylabel("Frequency")
plt.grid(axis='y', linestyle=':', linewidth=1, color='black')
plt.show()

#4. PIE CHART 
q1 = sum(info["unit"][0:3])
q2 = sum(info["unit"][3:6])
q3 = sum(info["unit"][6:9])
q4 = sum(info["unit"][9:12])

quarters = ["Q1","Q2","Q3","Q4"]
values = [q1,q2,q3,q4]
colors = ["red", "blue", "green", "purple"]

plt.figure(figsize=(5,3))
plt.pie(values, labels=quarters, autopct="%1.1f%%", startangle=90, colors=colors)
plt.title("Quarter-wise Unit Distribution")
plt.axis("equal")
plt.legend(title="Quarters")
plt.show()

# 5. SCATTER PLOT 
# Unit points
plt.scatter(info["months"], info["unit"], color='blue', label="Unit", s=80)

# Revenue points
plt.scatter(info["months"], info["revenue"], color='red', label="Revenue", s=80)

plt.title("Unit vs Revenue Scatter Plot")
plt.xlabel("Months")
plt.ylabel("Values")
plt.xticks(rotation=45)
plt.grid(True)

plt.legend()   # important to show labels
plt.show()