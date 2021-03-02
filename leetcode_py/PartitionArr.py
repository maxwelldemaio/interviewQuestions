def solve(k, numbers):
    # If k is 0, then whole array would work
    # If len of numbers is 0, then whole array would work
    if k == 0 or len(numbers) == 0:
        return "Yes"
    # If we can't break the array into k parts, return No
    if len(numbers) % k != 0:
        return "No"

    # Create frequency chart
    myCounter = {}
    for num in numbers:
        # Check if in frequency chart
        if num in myCounter:
            myCounter[num] += 1
        else:
            myCounter[num] = 1
    # If entry appears more times than how many times k goes into numbers
    # We would not have unique subsequences
    for entry in myCounter:
        if myCounter[entry] > len(numbers)/k:
            return "No"
    return "Yes"


if __name__ == '__main__':
    print(solve(3, [1, 2, 2, 3])) # no
    print(solve(2, [1, 2, 3, 4]))  # yes

    print(solve(2, [1, 2, 3, 3]))  # yes
    print(solve(3, [1, 2, 3, 4]))  # no
    print(solve(3, [3, 3, 3, 6, 6, 6, 9, 9, 9]))  # yes
    print(solve(1, []))  # yes
    print(solve(1, [1]))  # yes
    print(solve(2, [1, 2]))  # yes
