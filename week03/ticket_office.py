tickets_sold = 0
total_revenue = 0.0
free_tickets = 0

while True:
    name = input("Customer name (or q to quit): ")
    if name.lower() == 'q':
        break
    
    age = int(input("Age: "))
    if age < 0 or age > 120:
        print("Invalid age.")
        continue
        
    day = input("Day (weekday/weekend): ").lower()
    if day not in ["weekday", "weekend"]:
        print("Invalid day.")
        continue
        
    student = input("Student (yes/no): ").lower()
    if student not in ["yes", "no"]:
        print("Please answer yes or no.")
        continue

    # 1. Determine base price
    if day == "weekday":
        base_price = 200
    else:
        base_price = 250
        
    # 2. Determine discount and category based on rules order
    if age < 6:
        discount = 1.0  # 100%
        category = "Free"
    elif age >= 65:
        discount = 0.50 # 50%
        category = "Senior"
    elif 6 <= age <= 12:
        discount = 0.40 # 40%
        category = "Child"
    elif student == "yes" and age <= 25:
        discount = 0.30 # 30%
        category = "Student"
    else:
        discount = 0.0  # 0%
        category = "Standard"
        
    # 3. Calculate final price
    final_price = base_price * (1 - discount)
    
    # 4. Print ticket detail
    print(f"{name}: {final_price:.2f} TRY ({category})")
    
    # 5. Update summary totals
    tickets_sold += 1
    total_revenue += final_price
    if category == "Free":
        free_tickets += 1

# Print End Summary
if tickets_sold > 0:
    average_price = total_revenue / tickets_sold
    print(f"Tickets sold: {tickets_sold}")
    print(f"Total revenue: {total_revenue:.2f} TRY")
    print(f"Average price: {average_price:.2f} TRY")
    print(f"Free tickets: {free_tickets}")
else:
    print("No tickets sold.")