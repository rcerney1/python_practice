# logical operators evaluate multiple conditions or and not. not inverses

temp = 25
is_raining = False

if temp > 35 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is not cancelled")

temp2 = 0
is_sunny = True

if temp2 >= 28 and is_sunny:
    print("It is Hot outside, and its Sunny!")
elif temp2 <= 0 and is_sunny:
    print("It is cold outside, and its Sunny!")
elif 28 > temp > 0 and is_sunny:
    print("Its WARM outside and its Sunny!")