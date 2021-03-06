#You will be given a list of 32 bit unsigned integers. Flip all the bits 0->1 and 1->0 and return the result as an unsigned integer.
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    flipped=(int(n)^int('11111111111111111111111111111111',2))
    return flipped
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')
    
    fptr.close()
