import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("=== Student Marks Data Handling ===\n")

# Step 1: Take user input
n = int(input("Enter number of students: "))
m = int(input("Enter number of subjects: "))

# Enter subject names
subjects = []
for i in range(m):
    sub = input(f"Enter name of subject {i+1}: ")
    subjects.append(sub)

students = []
marks_list = []

for i in range(n):
    name = input(f"\nEnter name of student {i+1}: ")
    students.append(name)
    student_marks = []
    for sub in subjects:
        score = int(input(f"Enter marks in {sub} (0-100): "))
        student_marks.append(score)
    marks_list.append(student_marks)

# Convert to NumPy array
marks = np.array(marks_list)

# Step 2: Create DataFrame
df = pd.DataFrame(marks, columns=subjects)
df["Name"] = students
df = df[["Name"] + subjects]

print("\n=== Student Marks Data ===")
print(df)

# Step 3: NumPy analysis
print("\n=== NumPy Analysis ===")
print("Mean marks (overall):", np.mean(marks))
print("Median marks (overall):", np.median(marks))
print("Standard Deviation:", np.std(marks))

# Step 4: Pandas analysis
print("\n=== Pandas Analysis ===")
print("\nAverage marks per subject:")
print(df[subjects].mean())

df["Total"] = df[subjects].sum(axis=1)
print("\nTop 3 students by total marks:")
print(df.sort_values(by="Total", ascending=False).head(3))

print(f"\nStudents scoring above 80 in {subjects[0]}:")
print(df[df[subjects[0]] > 80])

df["Result"] = np.where(df[subjects].mean(axis=1) >= 50, "Pass", "Fail")
print("\nPass/Fail Results:")
print(df[["Name", "Result"]])

# Step 5: Save results
df.to_csv("student_results.csv", index=False)
print("\nData saved to 'student_results.csv'")

# =====================
# Step 6: Graph Menu
# =====================
while True:
    print("\n=== Graph Options ===")
    print("1. Bar Chart - Total Marks of Students")
    print("2. Line Chart - Subject-wise Average Marks")
    print("3. Pie Chart - Pass vs Fail Distribution")
    print("4. Show All Graphs")
    print("5. Exit (No Graphs)")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        plt.figure(figsize=(8,5))
        plt.bar(df["Name"], df["Total"], color="skyblue")
        plt.title("Total Marks of Students")
        plt.xlabel("Students")
        plt.ylabel("Total Marks")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
    elif choice == "2":
        plt.figure(figsize=(8,5))
        plt.plot(subjects, df[subjects].mean(), marker="o", linestyle="-", color="green")
        plt.title("Average Marks per Subject")
        plt.xlabel("Subjects")
        plt.ylabel("Average Marks")
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        
    elif choice == "3":
        plt.figure(figsize=(6,6))
        df["Result"].value_counts().plot.pie(autopct="%1.1f%%", colors=["lightgreen","lightcoral"])
        plt.title("Pass vs Fail Distribution")
        plt.ylabel("")
        plt.show()
        
    elif choice == "4":
        # Show all three graphs
        # Bar
        plt.figure(figsize=(8,5))
        plt.bar(df["Name"], df["Total"], color="skyblue")
        plt.title("Total Marks of Students")
        plt.xlabel("Students")
        plt.ylabel("Total Marks")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
        # Line
        plt.figure(figsize=(8,5))
        plt.plot(subjects, df[subjects].mean(), marker="o", linestyle="-", color="green")
        plt.title("Average Marks per Subject")
        plt.xlabel("Subjects")
        plt.ylabel("Average Marks")
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        
        # Pie
        plt.figure(figsize=(6,6))
        df["Result"].value_counts().plot.pie(autopct="%1.1f%%", colors=["lightgreen","lightcoral"])
        plt.title("Pass vs Fail Distribution")
        plt.ylabel("")
        plt.show()
        
    elif choice == "5":
        print("Exiting without showing graphs. ✅")
        break
    else:
        print("Invalid choice, please try again!")
