ceiling = 4 * 10**6
a = 1
b = 1
i = 0
total = 0
while(b < ceiling):
    tempb = b
    b += a
    print b
    a = tempb
    if (b % 2 == 0):
        total += b

print total
