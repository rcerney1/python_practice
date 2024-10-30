item = input("What item would you like to buy? ")
price = float(input("What is the price? "))
quantity = int(input("How many of them shits you need?"))

total = price * quantity

print(f"You have bought {quantity} X {item}/s")
print(f"the total is {total}")