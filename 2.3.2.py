import itertools


def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, num // 2, 2):
        if num % i == 0:
            return False
    return True


def prime():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


print(list(itertools.takewhile(lambda x: x <= 31, prime())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
