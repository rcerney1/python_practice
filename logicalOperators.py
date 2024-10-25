#logical operators
#or and not

temp = -25
isRaining = False



if temp > 35 or temp < 0 or isRaining:
    print("the outdoor event is canceled")
else:
    print("the outdoor event is still scheduled")

isSunny = True

if temp >= 28 and isSunny:
    print("it is sunny and hot")
elif temp <= 0 and isSunny:
    print("it is cold and sunny")
else:
    print("its not hot and sunny")