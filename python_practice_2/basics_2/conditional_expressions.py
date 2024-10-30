# conditional express = A one line shortcut for the ifelse statement (ternary operator)
a = 6
b = 7
age = 13
num = -5
temp = 20
user_role= "admin"

print("positive" if num > 0 else "negative")

result = "Even" if num % 2 == 0 else "Odd"

max_num = a if a > b else b
min_num = a if a < b else b

status = "Adult" if age >= 18 else "Child"

weather = "HOT" if temp > 30 else "COLD"

access_level = "Full Acess" if user_role == "admin" else "limited access"

print(result)
print(max_num)
print(min_num)
print(status)
print(weather)
print(access_level)