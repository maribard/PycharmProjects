'''try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except:
    print("Bład")'''



'''try:
    x = 5
    y = 0

    z = x / y
except:
    print("Błąd")
finally:
    print("All Done")'''




def ask():
    while True:
        try:
            number = int(input("Input an integer:"))
        except:
            print("Error. Try again")
        else:
            print("YES, your number is {}".format(number**2))
            break


ask()