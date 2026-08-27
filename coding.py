import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("student_data.csv")
print(df.head())

# Plot 1: Average Student Scores Over 10 Days
days = list(range(1, 11))
avg = [62, 64, 65, 68, 70, 71, 73, 75, 78, 80]

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(days, avg, marker="o", color='blue', linewidth=2)
ax.set_title("Average Student Scores Over 10 Days")
ax.set_xlabel("Days")
ax.set_ylabel("Average Score")
ax.grid(True)

plt.savefig('plot_scores.png', dpi=100, bbox_inches='tight')
print("Plot saved as plot_scores.png")

# Plot 2: Simple Line Plot
fig2, ax2 = plt.subplots(figsize=(8, 5))
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]
ax2.plot(x, y, marker='o', color='red', linewidth=2)
ax2.set_title("Line Plot")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.grid(True)

plt.savefig('plot_line.png', dpi=100, bbox_inches='tight')
print("Plot saved as plot_line.png")
fig3, ax3 = plt.subplots(figsize=(10, 6))
students = df['Name'].tolist()
marks = df['Marks'].tolist()

bars = ax3.bar(students, marks, color='green', alpha=0.7, edgecolor='black')
ax3.set_title("Student Marks Comparison", fontsize=14, fontweight='bold')
ax3.set_xlabel("Student Name", fontsize=12)
ax3.set_ylabel("Marks", fontsize=12)
ax3.set_ylim(0, 100)
ax3.grid(True, axis='y', alpha=0.3)
for bar in bars:
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height)}',
            ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig('plot_barchart.png', dpi=100, bbox_inches='tight')
print("Bar chart saved as plot_barchart.png")

fig4, ax4 = plt.subplots(figsize=(8, 8))
departments = df['Department'].value_counts()
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF99CC']

wedges, texts, autotexts = ax4.pie(departments.values, 
                                     labels=departments.index,
                                     autopct='%1.1f%%',
                                     colors=colors[:len(departments)],
                                     startangle=90,
                                     textprops={'fontsize': 11, 'weight': 'bold'})

ax4.set_title("Distribution of Students by Department", fontsize=14, fontweight='bold')

# Enhance the percentage text
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

plt.tight_layout()
plt.savefig('plot_piechart.png', dpi=100, bbox_inches='tight')
print("Pie chart saved as plot_piechart.png")

# Plot 5: Scatter Plot - Marks vs Attendance
fig5, ax5 = plt.subplots(figsize=(10, 6))
attendance = df['Attendance'].tolist()
marks = df['Marks'].tolist()

scatter = ax5.scatter(attendance, marks, c=marks, cmap='viridis', s=200, alpha=0.7, edgecolor='black', linewidth=2)
ax5.set_title("Student Marks vs Attendance", fontsize=14, fontweight='bold')
ax5.set_xlabel("Attendance (%)", fontsize=12)
ax5.set_ylabel("Marks", fontsize=12)
ax5.grid(True, alpha=0.3)

# Add colorbar
cbar = plt.colorbar(scatter, ax=ax5)
cbar.set_label('Marks', fontsize=11)

# Add value labels on each point
for i, student in enumerate(df['Name']):
    ax5.annotate(student, (attendance[i], marks[i]), 
                xytext=(5, 5), textcoords='offset points', fontsize=9)

plt.tight_layout()
plt.savefig('plot_scatter.png', dpi=100, bbox_inches='tight')
print("Scatter plot saved as plot_scatter.png")