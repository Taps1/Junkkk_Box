"""
Print uncommon elements from two sorted arrays
1.5
Given two sorted arrays of distinct elements, we need to print those elements from both arrays that are not common. The output should be printed in sorted order.

Examples:

Input : arr1[] = {10, 20, 30}
        arr2[] = {20, 25, 30, 40, 50}
        Output : 10 25 40 50
        We do not print 20 and 30 as these
        elements are present in both arrays.

        Input : arr1[] = {10, 20, 30}
                arr2[] = {40, 50}
                Output : 10 20 30 40 50
"""

[i for i in arr1+arr2 if (arr1+arr2).count(i)==1]
