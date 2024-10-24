#typecasting is the process of converting a variable from one data type to another

name = "Ryan Cerney"
age = 30
gpa = 3.8
isStudent = True

#get data type

print("types of data: ",type(name), type(age), type(gpa), type(isStudent))

#reassign age
print("\n\nNow for Age reassignment")
age = float(age)
print(f"age({age}) is now:", type(age))
age = str(age)
print(f"age({age}) is now:", type(age))
age = bool(age)
print(f"age({age}) is now:", type(age))