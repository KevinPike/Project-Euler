def isPalindrome(number):
    string = unicode(number)
    length = len(string)
    firstHalf = string[0:length/2]
    if (length % 2 != 0):
        secondHalf = string[length/2 + 1: length]
    else:
        secondHalf = string[length/2 : length]
    #reverse the string
    secondHalf = secondHalf[::-1]
    return firstHalf == secondHalf

digit = 2

rangeNum = range(10**digit, 10**(digit+1))
largestPalindrome = 0

for i in rangeNum:
    for j in rangeNum:
        test = i * j
        if (isPalindrome(test)):
            if (test > largestPalindrome):
                largestPalindrome = test

print largestPalindrome
