import math
import os
import random
import re
import sys

def bigSorting(unsorted):
    return sorted(unsorted, key=lambda x: (len(x), x))

if __name__ == '__main__':

    fptr = open("output.txt", "w")

    n = int(input().strip())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)


    fptr.write('\n'.join(result))
    fptr.write('\n')


    fptr.close()

print('\n'.join(result))