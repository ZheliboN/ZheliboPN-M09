
def is_prime(function):
    def wrapper(*args):
        res = function(*args)
        if res > 0:
            prime_number = True
            if res < 2:
                prime_number = True
            else:
                for i in range(2, res):
                    if res % i == 0:
                        prime_number = False
                        break
                    else:
                        prime_number = True
            if prime_number:
                print('Простое')
            else:
                print('Составное')
        return res
    return wrapper


@is_prime
def sum_three(a, b, c):
    res = a + b + c
    return res


result = sum_three(2, 3, 6)
print(result)

result = sum_three(9, 8, 7)
print(result)

result = sum_three(8, 11, 4)
print(result)

result = sum_three(0, 1, 0)
print(result)
