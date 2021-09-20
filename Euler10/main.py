# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


licznik = 3
suma = 2
while licznik < 2000000:
    licznik2 = 2
    while licznik % licznik2 != 0:
        licznik2 += 1
        if licznik == licznik2:
            suma += licznik
    licznik += 1
    print(licznik)


print(suma)