#while loops in python
x = 0
while x < 10:
    x += 1
    print(f"the number is {x}")

name = input("enter your name: ")

while name == "":
    name = input("Enter your name: ")

print(f"Hello, {name}")