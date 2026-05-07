# Problem 1.5, Page 5 — Division
# Label: exr:div
# An Introduction to the Analysis of Algorithms (4th Edition)

import sys

def div(x,y):
    
    #check pre-condition
    if x<0 or y<=0 or x!=int(x) or y!=int(y):
        raise ValueError('Invalid inputs for division.')
    
    #division algorithm
    q = 0
    r = x
    while y <= r:
        r -= y
        q += 1
    print(x,'=',q,'*',y,'+',r)
    print('so q =',q,'and r =',r)
    return (q,r)
    
if __name__ == '__main__':
    if len(sys.argv) > 3:
        raise TypeError('Too many inputs for division.')
    elif len(sys.argv) < 3:
        raise TypeError('Too few inputs for division.')
    else:
        div(int(sys.argv[1]),int(sys.argv[2]))