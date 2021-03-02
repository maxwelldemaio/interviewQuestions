def minswaps(arr):
    # Keep track of count of adj swaps
    # Keep track of number of swaps we need to move 1 to right
    result1 = 0
    unplaced_zeros = 0

    # Loop over arr and determine min adjacent swaps backwards
    for index in range(len(arr)-1, -1, -1):
        if arr[index] == 0:
            unplaced_zeros += 1
        else:
            result1 += unplaced_zeros
    
    result2 = 0
    unplaced_ones = 0
    for index in range(len(arr)-1, -1, -1):
        if arr[index] == 1:
            unplaced_ones += 1
        else:
            result2 += unplaced_ones

    if result1 < result2:
        return result1
    return result2


arr2 = [1, 0, 1, 0]
arr1 = [0, 0, 1, 0, 1, 0, 1, 1]
print(minswaps(arr2))
