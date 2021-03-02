#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'getNumberOfOptions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY priceOfJeans
#  2. INTEGER_ARRAY priceOfShoes
#  3. INTEGER_ARRAY priceOfSkirts
#  4. INTEGER_ARRAY priceOfTops
#  5. INTEGER budgeted
#

# 19:38 check if
def getNumberOfOptions(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, budgeted):
    # Make 0(n^2) flat array of jeans+shoes
    jeansAndShoes = []
    for jean in priceOfJeans:
        for shoe in priceOfShoes:
            jeansAndShoes.append(jean + shoe)
    
    # Make 0(n^2) flat array of skirts+tops
    skirtsAndTops = []
    for skirt in priceOfSkirts:
        for top in priceOfTops:
            skirtsAndTops.append(skirt + top)

    # Sort
    jeansAndShoes.sort()
    skirtsAndTops.sort(reverse=True)

    # Combinations and pointer
    result = 0
    limit = 0
    for cost in jeansAndShoes:
        remaining = budgeted - cost
        while limit < len(skirtsAndTops) and skirtsAndTops[limit] > remaining:
            limit += 1
        if limit == len(skirtsAndTops):
            break
        result += len(skirtsAndTops) - limit

    return result


# Sorted: [4], [1, 3, 4], [2, 3], [4]
print(getNumberOfOptions([4], [3, 4, 1], [3, 2], [4], 12))  # 2
print(getNumberOfOptions([7, 8, 9, 1, 8, 6, 14], [10, 5, 7], [5, 6, 6, 4, 8, 8], [3, 12, 11, 3], 30))  # 314

