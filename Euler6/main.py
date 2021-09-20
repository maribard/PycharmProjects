# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


i = 1
j = 1
value1 = 0
value2 = 0

while i <= 100:
    value1 += i ** 2
    i += 1

#print(value1)

while j <= 100:
    print(str(j))
    print(value2)
    print()
    value2 += j
    j += 1

print(value2)

print(str(value2**2-value1))