sum3 = 0
sum5 = 0
num3 = 3
num5 = 5
ceiling = 1000
while(num3 < ceiling or num5 < ceiling):
    if (num3 < ceiling and num3 % 5 != 0):
        sum3 += num3
    if (num5 < ceiling):
        sum5 += num5
        num5 += 5
    num3 += 3
print(sum3 + sum5)
