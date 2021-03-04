def find_sum_iter(n):
    """Iterative approach"""
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

def find_sum_rec(n):
    # Base condition
    if n == 1:
        return 1
    return n + find_sum_rec(n - 1)


if __name__ == "__main__":
    print(find_sum_rec(5))