order_total = 247

print("order total: ", order_total)

if order_total > 100:
    discount = 25
else:
    discount = 0

print("\nif order_total > 100:\n"
      "    discount = 25\n"
      "else:\n"
      "    discount = 0\n")

print("order total: ", order_total,
      "\ndiscount: ", discount)

discount = 50 if order_total > 200 else 0
print("\ndiscount = 50 if order_total > 200 else 0\n"
      "discount: ", discount)
