from math import factorial

def FindSumOfString(string):
    try:
        if (len(string) == 1):
            return int(string[0])
        return int(string[0]) + FindSumOfString(string[1:len(string)])
    except ValueError:
        return None

print FindSumOfString(str(factorial(100)))
