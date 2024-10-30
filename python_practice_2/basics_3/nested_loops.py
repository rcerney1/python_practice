# nested loop =  A loop within anouther loop (outer, inner)
#                outer loop:
#                   inner loop:

for x in range(3):
    for y in range(1, 10):
        print(y, end="")
    print()

rows = int(input("Enter the number or rows: "))
columns = int(input("Enter the number or columns: "))
symbol = input("enter a symbol: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()