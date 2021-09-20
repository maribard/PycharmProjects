# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


value = 600851475143
last_factor = 0.5

while value / last_factor != 1:
    i = 2
    while value % i != 0:
        i += 1
    print(i)
    value = value / i
    last_factor = i
    if value == 1:
        break


