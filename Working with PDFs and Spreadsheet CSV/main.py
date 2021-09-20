def is_prime(number):
    i = 2
    while i < number:
        if number % i == 0:
            return False
        else:
            pass
        i += 1
    return True


def generate_prime(current_prime):
    while True:
        current_prime = current_prime +1
        if is_prime(current_prime) == True:
            return current_prime
        else:
            pass

current_prime_number = 2

while True:
    print( current_prime_number )
    answer = input("Would you like to see next prime: ")
    if answer.lower().startswith('y'):
        current_prime_number = generate_prime(current_prime_number)
    else:
        break