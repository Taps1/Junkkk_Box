"""
Find nth number that contains the digit k or divisible by k
You've given 2 numbers n & k, need to find n-th number that contains the digit k or divisible by k (2 <= k <=9)

Input: n=15, k=3
Output: 33
Exploitation: (3,6,9,12,13,15,18,21,23,24,27,30,31,32,33)
33 is the 15th number
"""

import sys

def problem_1(n, k):
    if k<2 or k>9:
        raise ValueError("Arguments supplied are not proper")
        sys.exit()
    flag = True; i = 1; result = [];
    while flag:
        if str(k) in str(i) or i%k==0:
            result.append(i)
        if len(result) >= n:
            flag = False
        i += 1
    print "Result is: ", result[n-1]

if __name__ == "__main__":
    n, k = sys.argv[1:]
    problem_1(int(n), int(k))
