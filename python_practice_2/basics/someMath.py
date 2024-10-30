import math

radius = float(input("Enter the radius of a circle: "))

circumference = 2 * math.pi * radius
area = math.pi * (radius**2)

print(f"The circumference given the radius you provided is {circumference}")
print(f"The area is {round(area,2)}cm2")


a = float(input("Enter side a: "))
b = float(input('Enter side b: '))
c = math.sqrt(pow(a,2) + pow(b, 2))

print(f"side c is {round(c, 2)}")

