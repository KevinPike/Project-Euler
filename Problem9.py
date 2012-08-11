total = 1000

def IsPythagorean(a, b, c):
    return (a**2 + b**2) == c**2

def AddsToTotal(a, b, c):
    return a + b + c == total

def Find():
    for i in range(1, total):
    
        for j in range(i, total):

            for k in range(j, total):
#                print '{} {} {}'.format(i,j,k)
                if (IsPythagorean(i,j,k) and AddsToTotal(i,j,k)):
                    print i*j*k
                    return

Find()
