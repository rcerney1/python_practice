#format specifiers = {value:flags} format a value based on what flags are inserted

#.(number)f = round to that many decimal plcaes
# :(number) = allocate that many spaces
# :03 = allocated and zero pda that many spaces
# etc


price1 = 3.14159
price2 = -987.253
price3 = 12.34

print(f"Price 1 is {price1:10}")
print(f"Price 2 is {price2:.1f}")
print(f"Price 3 is {price3:.1f}")