# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


value = 2000
j = True

while j:
    value += 1
    i = 20
    print(value)
    while value % i == 0:
        print("hej")
        i = i - 1
        if i == 1:
            break
    if i == 1:
        j = False


print(value)