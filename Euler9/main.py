import math
#a = 16
#(a)
#pierwiastek = math.sqrt(a)
#print('pierwiastek z a wynosi: ' + repr(pierwiastek))

a = 3
b = 4
good_a = 0
good_b = 0
good_c = 0

while a != 600:
    while b != 600:
        suma = a**2 + b**2
        if math.sqrt(suma) + a + b == 1000 and a < b:
            good_a = a
            good_b = b
            good_c = math.sqrt(suma)
        b += 1
    a += 1
    b = 4

print("a = " + str(good_a))
print("b = " + str(good_b))
print("c = " + str(good_c))
liczba = good_a * good_c * good_b

print(liczba)


#algorytm na to czy liczba jest calkowitą:
#czy ma w sobie kropkę
#jeżeli ma, to czy string po kropce jest równy "0"