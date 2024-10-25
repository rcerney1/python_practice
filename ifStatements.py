age = int(input("enter your age: "))
price = 10

if age >= 65:
    print("you are a senior")
    print(f"the ticket price for a senior is ${float(price * .75)}")
elif age >= 18:
    print("you are an adult")
    print(f"the ticket price for an adult is ${float(price)}")
else:
    print("you are a child")
    print(f"the ticket price for a child is ${price * .5}")


if age >= 18 and age < 60:
    print("you are an adult")

