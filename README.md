# Week 1 Lab
- Test: I filled out all the inputs with sample data and the student card printed successfully.
- Change: After testing, I organized the repository folders according to the lab instructions.

# Week 2 Lab
- Test: Tested with 2x50 and 1x80 items, delivery 20, tax 10%. Final total verified as 218.00 TRY.
- Change: Formatted money values to show 2 decimal places using f-strings (:.2f).

## Week 03

**What did you change?:** AI'ın verdiği kodda değişken isimlerini inceleyip mantığını anladım, testlerimi yaparak çalıştığından emin oldum.
**Tests:**
1. Ali, Yaş 30, weekend, no -> Beklenen: 250.00 TRY (Standard)
2. Can, Yaş 5, weekend, no -> Beklenen: 0.00 TRY (Free)
3. Zeynep, Yaş 12, weekday, no -> Beklenen: 120.00 TRY (Child) - *Boundary age test (sınır yaş testi)*
**Why does the order of the rules matter?:** Kuralların sırası önemlidir çünkü if/elif yapısında program doğru (True) olan ilk koşulu çalıştırır ve gerisine bakmaz. Eğer Öğrenci (Student) kuralını Çocuk (Child) kuralından önce yazsaydık, 10 yaşındaki öğrenci olan bir çocuk %40 yerine %30 indirim alıp haksızlığa uğrardı.

GitHub1
Your Name: FURKAN AYAN
Your Student Number: 2604109500
Your Department: Management Information Systems
Course Name: MIS203 Basic Programming

### AI Tool Usage Note
**AI Tool Used:** Gemini
**Prompt Used:** "Help me create a simple Python program that asks the user for their Name, Department, Age, and Career Goal, and then prints a short student profile. Also, help me prepare the README.md file in English for my GitHub assignment."
**What did you change?:** I reviewed the generated Python code, tested it in my local environment, and updated the README file with my personal student details.
