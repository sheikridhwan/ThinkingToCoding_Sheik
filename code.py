items = []
n  = int(input("enter the number of items: "))


for i in range(1,n+1):
    name = input(f"enter name of item {i}: ")
    price = float(input(f"enter price of {name}: "))
    quantity = int(input(f"enter quantity of {name}: "))
    items.append((name, price, quantity))


subtotal = 0
print("\n---------------------------------------")
print("           MINI BILL CALCULATOR          ")
print("-----------------------------------------")
print(f"{'item':<13}{'price':>8}{'qty':>6}{'subtotal':>12}")

for item in items:
    name, price, quantity = item
    item_total = price * quantity
    subtotal += item_total
    print(f"{name:<13}{price:>8}{quantity:>6}{item_total:>6}")

tax = subtotal * 0.1
total = subtotal + tax

print("-----------------------------------------")
print(f"{'subtotal:':>29}{subtotal:>12}")
print(f"{'tax':>29}{tax:>12}")
print("------------------------------------- ----")
print(f"{'total:':>29}{total:>12}")

