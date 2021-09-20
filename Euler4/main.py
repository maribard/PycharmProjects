# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

i = 1
j = 1
lista_palindromow = []
while i < 1000:
    j = 1
    while j < 1000:
        kandydat = str(i*j)
        if kandydat == kandydat[::-1]:
            lista_palindromow.append(int(kandydat))
        j += 1
    i += 1

print(lista_palindromow)
print(max(lista_palindromow))