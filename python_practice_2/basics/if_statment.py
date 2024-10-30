# if statements - do code only if some condition is true
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
elif age < 0:
    print("you are not alive yet")
else:
    print("You are not an adult")


#example 1
response = input("Would you like some food? (Y/N): ")

if response == "Y" or response == "y":
    print("Have some food!")
elif response =="N" or response == "n": 
    print("No food for you!")
else:
    print("You did it wrong, idiot")