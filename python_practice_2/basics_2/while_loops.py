name = input("Enter your name: ")

while name == "":
    print("you didnt type anything")
    name = input("Enter your name: ") #input gives a chance to escape infinit loop



age = int(input("Enter your age: "))

while age < 0:
    print("Please enter a valid age")
    age = int(input("Enter your age: "))


food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"you like {food}")
    food = input("Enter another food you like: ")

print(f"Goodbye {name} who is {age} years old")


num = int(input("Enter a number between 1 and 10: "))

while num < 1 or num > 10:
    print("Your number is not valid")
    num = int(input("Enter a new number:" ))