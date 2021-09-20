# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


var1 = 1
var2 = 2
print(var1)
print(var2)


lista = [1, 2]


lenght = len(lista)
new_element = 0
sum_values = 2
while new_element < 4000000:
    new_element = lista[lenght-1] + lista[lenght-2]
    if new_element > 4000000:
        break
    #print(new_element)
    if new_element % 2 == 0:
        print(new_element)
        sum_values += new_element
    lista.append(new_element)
    lenght = len(lista)


print(lista)
print(sum_values)