###
# Euler Project Problem 10

def isPrime(integer):
    i = 2
    while (i <= integer**.5):
        if (integer % i == 0):
            return False
        i += 1
    return True

num = 2 * 10**6

start = 3
total = 2

while (start < num):
    if (isPrime(start)):
        total += start
    start += 2

print total

