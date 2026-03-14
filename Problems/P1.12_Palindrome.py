# Problem 1.12, Page 8 — Palindrome
# Label: exr:palinpython
# An Introduction to the Analysis of Algorithms (4th Edition)

import sys

def isPalindrome(x):
    n = len(x)
    i = 0
    while i < int(n/2):
        if x[i]!=x[n-i-1]:
            print('"',str(x),'" IS NOT a palindrome.')
            return False
        i += 1
    print('"',str(x),'" IS a palindrome.')
    return True

#above we have algorithm 1.3 defined explicitly as it is in the text.
#below, we have the slice equivalent of the above.

def isPal(x):
    n = len(x)
    if x[:int(n/2):1] == x[-1:-int(n/2)-1:-1] :
        print('"',str(x),'" IS a palindrome.')
        return True
    else:
        print('"',str(x),'" IS NOT a palindrome.')
        return False


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        try:
            isPal(eval(arg))
        except:
            isPal(arg)