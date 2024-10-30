#2D lists is just a list of lists

fruits = ["apple", "oranges", "banana", "pear"]
vegetables = ["broccoli", "spinach", "carrots"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

print(f"the first item in the first list is at index [0][0] and is: {groceries[0][0]}")

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()