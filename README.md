# Week 1 Lab
- Test: I filled out all the inputs with sample data and the student card printed successfully.
- Change: After testing, I organized the repository folders according to the lab instructions.

# Week 2 Lab
- Test: Tested with 2x50 and 1x80 items, delivery 20, tax 10%. Final total verified as 218.00 TRY.
- Change: Formatted money values to show 2 decimal places using f-strings (:.2f).

### Week 03

**AI Tool Used:** Gemini
**Prompt Used:** "Help me write a Python program for a cinema ticket office that calculates prices based on age, day, and student status using loops and conditions, and update my README file for Week 03."
**What did you change?:** I reviewed the conditions and loop structure to ensure it perfectly matches the exact output format and rules requested in the assignment. I also tested the boundary limits.

**Tests:**
1. Input: Age 150 -> Result: "Invalid age." (Boundary test)
2. Input: Age 26, weekday, Student yes -> Result: "200.00 TRY (Standard)" (Tests student age limit)
3. Input: Age 5, weekend, Student no -> Result: "0.00 TRY (Free)" (Tests under 6 boundary)

**Why does the order of the rules matter?:**
The order of the rules matters because the `if/elif` structure executes the very first condition that evaluates to True and skips the rest. If the "Student" rule was placed before the "Child" rule, a 10-year-old student would trigger the 30% student discount instead of getting the 40% child discount, resulting in the customer overpaying.

GitHub1
Your Name: FURKAN AYAN
Your Student Number: 2604109500
Your Department: Management Information Systems
Course Name: MIS203 Basic Programming

### AI Tool Usage Note
**AI Tool Used:** Gemini
**Prompt Used:** "Help me create a simple Python program that asks the user for their Name, Department, Age, and Career Goal, and then prints a short student profile. Also, help me prepare the README.md file in English for my GitHub assignment."
**What did you change?:** I reviewed the generated Python code, tested it in my local environment, and updated the README file with my personal student details.
