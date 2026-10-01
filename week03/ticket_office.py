# Initialize variables to keep track of sales
tickets_sold = 0
total_revenue = 0.0
free_tickets = 0

while True:
    # 1. Ask for name and check for quit
    name = input("Customer name (or q to quit): ")
    if name.lower() == 'q':
        break
    
    # 2. Ask for age and validate boundaries
    age = int(input("Age: "))
    if age < 0 or age > 120:
        print("Invalid age.")
        continue
        
    # 3. Ask for day and validate
    day = input("Day (weekday/weekend): ").lower()
    if day != "weekday" and day != "weekend":
        print("Invalid day.")
        continue
        
    # 4. Ask for student status and validate
    student = input("Student (yes/no): ").lower()
    if student != "yes" and student != "no":
        print("Please answer yes or no.")
        continue
        
    # 5. Determine base price
    if day == "weekday":
        base_price = 200
    else:
        base_price = 250
        
    # 6. Apply discount rules in strict order
    if age < 6:
        discount = 1.0
        ticket_type = "Free"
    elif age >= 65:
        discount = 0.50
        ticket_type = "Senior"
    elif 6 <= age <= 12:
        discount = 0.40
        ticket_type = "Child"
    elif student == "yes" and age <= 25:
        discount = 0.30
        ticket_type = "Student"
    else:
        discount = 0.0
        ticket_type = "Standard"
        
    # Calculate final price
    final_price = base_price * (1 - discount)
    
    # Print the individual ticket result
    print(f"{name}: {final_price:.2f} TRY ({ticket_type})")
    
    # Update summary statistics
    tickets_sold += 1
    total_revenue += final_price
    if ticket_type == "Free":
        free_tickets += 1

# 7. Print summary after the loop ends
if tickets_sold == 0:
    print("No tickets sold.")
else:
    avg_price = total_revenue / tickets_sold
    print(f"Tickets sold: {tickets_sold}")
    print(f"Total revenue: {total_revenue:.2f} TRY")
    print(f"Average price: {avg_price:.2f} TRY")
    print(f"Free tickets: {free_tickets}")
