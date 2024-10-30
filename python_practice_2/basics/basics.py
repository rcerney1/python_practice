#variables - Integer, string, float, boolean
age = 30
name = "Ryan"
gpa = 4.5
isDope = True #uppercase True or Flase

print(f" number: {age} \n name: {name}\n gpa: {gpa}\n they dope? {isDope}")


#typecasting, converting a variable from one datatype to another

age = str(age)
# name = int(name) #invalid

number = 25
number = str(number)
print(type(number))
number = int(number)
print(type(number))

#input() = a function that promps the user to enter data

userName = input("what is your name? ")
userAge = input("How old are you? ")

print(f"age is type of {type(userAge)}")
#inputs are takin in as strings

print(f"Hello, {userName}. you are {userAge} year(s) old")
