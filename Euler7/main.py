# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
boolean = True
boolean2 = True
liczba = 2
dzielnik = 2
licznik = 1


while  boolean == True:
    while liczba % dzielnik != 0:
        dzielnik += 1
        if liczba == dzielnik:
            licznik += 1
            print("liczba: " + str(liczba) + "   z kolei: " + str(licznik))
            break
    if licznik == 10001:
        break
    liczba += 1
    dzielnik = 2

