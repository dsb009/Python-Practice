#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def sockMerchant(n, ar):
    # Write your code here
    number_of_pairs=0
    counts = Counter(ar) 
    for i in counts.values():
        number_of_pairs = number_of_pairs + int((i/2))
    return number_of_pairs
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
