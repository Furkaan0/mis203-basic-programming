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
