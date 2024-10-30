#for loops = execute a block of code a fixed number of times. 
#            can iterate over a range, string, sequence, etc


#iterate through a range
for x in range(1, 11):
    print(x)

#reverse countdown
for countdown in reversed(range(1,11)):
    print(countdown)

print("Happy New Year!")


#skip the number of 13
for y in range(1, 21):
    if y == 13:
        continue
    else:
        print(y)