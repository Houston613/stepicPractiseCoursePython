s, a, b = (input() for i in range(3))


def func(x, y, z, count=0):
    while y in x:
        x = x.replace(y, z)
        count += 1
        if count >= 1000:
            return 'Impossible'
    return count


func(s, a, b)
