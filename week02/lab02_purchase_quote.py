# lab02_purchase_quote.py

print("--- Two-Item Purchase Quote Calculator ---\n")

# 1. Ürün 1 Bilgileri
item1_name = input("Enter item 1 name: ")
item1_qty = int(input("Enter item 1 quantity: "))
item1_price = float(input("Enter item 1 unit price: "))

# 2. Ürün 2 Bilgileri
item2_name = input("Enter item 2 name: ")
item2_qty = int(input("Enter item 2 quantity: "))
item2_price = float(input("Enter item 2 unit price: "))

# 3. Kargo ve Vergi Bilgileri
delivery_fee = float(input("Enter delivery fee: "))
tax_percentage = float(input("Enter tax percentage (e.g., 10 for 10%): "))

# 4. Hesaplamalar
line1_total = item1_qty * item1_price
line2_total = item2_qty * item2_price
subtotal = line1_total + line2_total

tax_amount = subtotal * (tax_percentage / 100)
final_total = subtotal + tax_amount + delivery_fee

# 5. Çıktı (Fatura/Teklif Kartı)
print("\n" + "=" * 48)
print("               PURCHASE QUOTE")
print("=" * 48)
print(f" {item1_qty}x {item1_name} (@ {item1_price:.2f}) : {line1_total:.2f} TRY")
print(f" {item2_qty}x {item2_name} (@ {item2_price:.2f}) : {line2_total:.2f} TRY")
print("-" * 48)
print(f" Subtotal           : {subtotal:.2f} TRY")
print(f" Tax ({tax_percentage}%)       : {tax_amount:.2f} TRY")
print(f" Delivery Fee       : {delivery_fee:.2f} TRY")
print("=" * 48)
print(f" FINAL TOTAL        : {final_total:.2f} TRY")
print("=" * 48)
