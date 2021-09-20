'''
def old_macdonald(name):
    name = list(name)
    name[0] = name[0].upper()
    name[3] = name[3].upper()
    return ''.join(name)

print(old_macdonald('macdonald'))
'''


'''
def master_yoda(text):
    lista = list("".join(text))
    return lista[::-1]

print(master_yoda('I am home'))
print(master_yoda('We are ready'))
'''

'''
def almost_there(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
    '''

'''
def has_33(nums):
    i = 0
    while i < len(nums)-1:
        if nums[i] == 3 and nums[i+1] == 3:
            return True
        i += 1
    return False

print(has_33([3, 1, 3]))
'''

'''
def paper_doll(text):
    lista = "".join(text)
    lista2 = [x*3 for x in lista]
    return "".join(lista2)

print(paper_doll('Hello'))
'''

'''
def blackjack(a,b,c):
    suma = a + b + c
    if suma <= 21:
        return suma
    elif suma > 21:
        if a == 11 or b == 11 or c == 11:
            if suma - 10 > 21:
                return 'BUST'
            elif suma - 10 < 21:
                return suma - 10
        else:
            return 'BUST'

print(blackjack(9,9,11))
'''



'''
def summer_69(arr):
    help_el = True
    for index, x in enumerate(arr):
        if x == 6:
            help_el = False
            arr[index] = 0
            continue
        if x == 7 or x == 8 or x == 9:
            if help_el == False:
                arr[index] = 0
                continue
        else:
            help_el = True
    return sum(arr)



print(summer_69([4, 5, 6, 7, 8, 9, 11, 7, 6, 7, 6, 6, 8, 1]))
'''


'''
def spy_game(nums):
    first = True
    second = False
    third = False
    for x in nums:
        if x == 0 and first:
            second = True
            first = False
            continue
        if x == 0 and second:
            third = True
            second = False
            continue
        if x == 7 and third:
            return True
    return False


print(spy_game([1,7,2,0,4,5,0]))
'''


'''
def count_primes(num):
    ilosc = 1
    for x in range(3, num):
        for y in range(2, x):
            if x % y == 0:
                break
            if y == x - 1:
                ilosc += 1
    return ilosc

print(count_primes(100))
'''


'''
def old_macdonald(name):
    name = list(name)
    name[0] = name[0].upper()
    name[3] = name[3].upper()
    return ''.join(name)

print(old_macdonald('macdonald'))
'''


'''
def master_yoda(text):
    lista = list(text.split(' '))
    return lista[::-1]

print(master_yoda('I am home'))
print(master_yoda('We are ready'))'''

