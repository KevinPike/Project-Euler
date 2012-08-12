def Has500Divisors(number):
    divisors = list()
    sqrt = number**.5
    try:
        intSqrt = int(round(sqrt))
    except ValueError:
        return None
    for i in range(1, intSqrt):
        if (number % i != 0):
            continue
        temp = number / i
        if (not divisors.count(temp)):
            divisors.append(temp)
        if (not divisors.count(i)):
            divisors.append(i)
    return len(divisors) >= 500

triangle = 0
for i in range(1,10**8):
    triangle += i
    if (Has500Divisors(triangle)):
        print triangle
        break
