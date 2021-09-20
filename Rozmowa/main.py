'''
poziom = 0

j = 0
def myfunc(lista, poziom, j):
    for l in lista:
        if l == []:
            poziom += 1
            i = 0
            while (i <= poziom):
                print("\t", end=' ')
                i += 1
            print("[]")
            poziom -= 1
        elif isinstance(l, list):
            poziom += 1
            j, poziom = myfunc(l, poziom, j)
            poziom -= 1
            if l == lista[-1]:
                j = 1
        else:
            i = 0
            if l == lista[0] and j == 0:
                print()
            if l == lista[0] or j == 1:
                while (i <= poziom):
                    #print("\t" + "poziom" + str(poziom), end=' ')
                    print("\t", end=' ')
                    i += 1
                print(str(l), end=' ')
            else:
                print(str(l), end=' ')
            j = 0
            if l == lista[-1] or l == []:
                j += 1
                print()
    return j, poziom



L = [9,[88,[4,7], [[],[]], 6],[7, 8, 9],77]
myfunc(L, poziom, j)
'''

'''
lista = [1,2,3,4,5,6,7,8,9]
lista2 = [x for x in lista[::-1] if x%2 == 0]
print(lista2)

'''

'''
import sys

print("Argument:", sys.argv[1])
'''


'''
def new_decorator(origin_function):
    def wrap_func():
        print("Some extra code1")
        origin_function()
        print("Some extra code2")
    return wrap_func

@new_decorator
def func_needs_decorated():
    print("I want to be decorated")


func_needs_decorated()'''




"""
def my_gen(n):
    for x in range(n):
        yield x



for number in my_gen(10):
    print(number)
"""

















