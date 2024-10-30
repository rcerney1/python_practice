import math

friends = 0

friends = friends + 1
friends += 1

friends = friends - 2
friends -= 2

friends = friends * 3
friends *= 3

friends = friends / 2
friends /= 2

friends = friends ** 2
friends **= 2

remainder = friends % 2
#print(friends, remainder)

## built in math functions

x = 3.14
y = 4
z = 5

resultX = round(x)
resultY = abs(y)
power = pow(4, 3)
resultMax = max(x, y, z)
resultMin = min(x, y, z)
print(resultX, resultY, power, resultMax, resultMin)
print(math.pi)

resultSquare = math.sqrt(9)
print(resultSquare)

resultCeil = math.ceil(9.6)
resultFloor = math.floor(9.6)
print(resultCeil, resultFloor)