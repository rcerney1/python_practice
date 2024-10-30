name = input("Enter your full name: ")
name_parts = name.split(" ")
print(name_parts)
num_characters = len(name)
first_space = name.find(" ")



print(f"\nName: {name}\nNumber of characters: {num_characters}\n{first_space}")
print(f"proper name: {name.capitalize()}")
print(f"big name: {name.upper()}")


username = input("Enter a username (no spaces, numbers, must be under 12 characeters): ")

username.find(" ")

if len(username) > 12:
    print("username is too long!")
elif not username.find(" ") == -1:
    print("No spaces!")
elif not username.isalpha():
    print("No numbers!")
else: 
    print(f"welcome, {username}")



