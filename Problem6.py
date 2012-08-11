r = 100

def SumSquares(top):
    if (top == 1):
        return 1
    return top**2 + SumSquares(top - 1)

def SquareSum(top):
    return Sum(top)**2

def Sum(top):
    if (top == 1):
        return 1
    return top + Sum(top - 1)

print SquareSum(r) - SumSquares(r)
