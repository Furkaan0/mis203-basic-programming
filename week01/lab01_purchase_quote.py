# lab01_student_card.py

print("Please fill out the information below:\n")

# 1. Get user input
name = input("Full Name: ")
student_id = input("Student ID: ")
department = input("Department: ")
github_username = input("GitHub Username: ")
programming_goal = input("What is your one programming goal?: ")

# 2. Print a clean student card
print("\n" + "=" * 45)
print("           STUDENT INTRODUCTION CARD")
print("=" * 45)
print(f" Full Name      : {name}")
print(f" Student ID     : {student_id}")
print(f" Department     : {department}")
print(f" GitHub         : @{github_username}")
print(f" Goal           : {programming_goal}")
print("=" * 45)
