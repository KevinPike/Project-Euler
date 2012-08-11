###
# ProjectEuler.net Problem 7

def isPrime(integer):
    i = 2
    while (i <= integer**.5):
        if (integer % i == 0):
            return False
        i += 1
    return True

count = 1
start = 1
size = 10001

while(count < size):
    start += 2
    if (isPrime(start)):
        count += 1

print 'The 10001st prime number is {}'.format(start)
