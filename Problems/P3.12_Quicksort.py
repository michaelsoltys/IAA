# Problem 3.12, Page 69 — Quicksort
# Label: exr:quicksort
# An Introduction to the Analysis of Algorithms (4th Edition)

from copy import copy


#takes an list of objects with defined <=
def quicksort(input_list):
    if len(input_list) <= 1:
        return input_list
    else:
        A = copy(input_list)
        x = A.pop()
        small = []
        large = []
        for a in A:
            if a <= x:
                small.append(a)
            else:
                large.append(a)
        return quicksort(small) + [x] + quicksort(large)


#main first attempts to evaluate inputs before sorting.
#if this fails it sorts them using the string <= for comparison.
if __name__ == '__main__':
    while True:
        inp = input('Enter a comma-separated list:\n... ')
        args = [arg.replace(' ','') for arg in inp.split(',') if arg]
        if args[0] in ['q','quit','Quit','QUIT']:
            break
        try:
            args = [eval(arg) for arg in args]
            print('\n',quicksort(args),'\n')
        except:
            try:
                print('\n',quicksort(args),'\n')
            except:
                print('Unorderable inputs.')