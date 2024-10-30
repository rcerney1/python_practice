# temp convertor

unit = input("Is tis temp in C or F: ")
temp = float(input("Enter the temp: "))

if unit == "C" or unit == "c":
    temp = round(((9 * temp) / 5) + 32, 1)
elif unit == "F" or unit == "f":
    temp = round((temp - 32) * 5 / 9, 1)

