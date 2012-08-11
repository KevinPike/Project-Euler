maximum = 20

divisors = range(1, maximum)[::-1]

answer = maximum
nope = False

while(True):
    for divisor in divisors:
        if (answer % divisor != 0):
            nope = True
            break
        else:
            nope = False
    if (nope):
        answer += 1
    else:
        break

print answer
