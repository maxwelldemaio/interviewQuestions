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

def getNumberOfOptions(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, budgeted):
    print("My input", priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, budgeted)
    # Check combinations
    combCount = 0
    currPrice = 0
    for jPrice in priceOfJeans:
        currPrice = jPrice
        subTot1 = currPrice

        if currPrice <= budgeted:
            for sPrice in priceOfShoes:
                currPrice = subTot1 + sPrice
                subTot2 = currPrice

                if currPrice <= budgeted:
                    for kPrice in priceOfSkirts:
                        currPrice = subTot2 + kPrice
                        subTot3 = currPrice
                        if currPrice <= budgeted:
                            for tPrice in priceOfTops:
                                currPrice = subTot3 + tPrice
                                if currPrice <= budgeted:
                                    combCount += 1
                                    currPrice = 0

    return combCount

# Sorted: [4], [1, 3, 4], [2, 3], [4]
print(getNumberOfOptions([4], [3, 4, 1], [3, 2], [4], 12)) #2
print(getNumberOfOptions([7, 8, 9, 1, 8, 6, 14], [10, 5, 7], [5, 6, 6, 4, 8, 8],[3, 12, 11, 3], 30)) # 314
