num = 600851475143
#num = 13195

i = 2
factor = i

def isPrime(integer):
    i = 2
    while (i < integer**.5):
        if (integer % i == 0):
            print '{} isnt prime factor: {}'.format(integer, i)
            return False
        i += 1
    return True

while (i <= num**.5):
    if (num % i == 0 and isPrime(i)):
        factor = i
        print factor
    i += 1

print factor

