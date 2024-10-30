# collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates ok
# Set = {} unordered and immutable, but add/remove ok - no duplicated
# Tuple = () ordered and unchangeable. duplicates ok Faster


fruit = "apple"
print(f"fruit: {fruit}") # -----> fruit: apple

#! LISTS !#
#List
fruits = ["apple", "mango", "orange"]
print(f"fruits: {fruits}") # ---> fruits: ['apple', 'mango', 'orange']

#adds to end of list
fruits.append("appended")
print(f"fruits: {fruits}") # ---> fruits: ['apple', 'mango', 'orange', 'appended']

#reverses List
fruits.reverse()
print(f"fruits: {fruits}")

#sorts alphebitically
fruits.sort()
print(f"fruits: {fruits}")

#clears list
fruits.clear()
print(f"fruits: {fruits}")

#! Sets
fruit_set = {"apple", "orange", "mango"}
print(f"fruit set: {fruit_set}")

fruit_set.add("pineapple")
print(f"fruit set: {fruit_set}")

#! Tuples
fruit_tuple = ("apple", "pear", "coconut")
print(f"fruit tuple: {fruit_tuple}")
print(fruit_tuple.count("apple"))