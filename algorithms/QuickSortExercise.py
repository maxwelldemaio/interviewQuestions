def swap(a, b, arr):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp


def partition(elements, start, pivot_index):
    """Lumuto partitioning scheme"""
    pivot = elements[pivot_index]

    # Move until we find a number > pivot
    while elements[start] < pivot:
        while start < len(elements) and elements[start] < pivot:
            start += 1
        # Set i equal to the starter pivot and look for number < pivot
        i = start
        while i < len(elements) and elements[i] > pivot:
            i += 1
        if start < i:
            # swap start/end
            swap(start, i, elements)
    # Return where we swapped pivot to (if so)
    if start == pivot_index:
        return start - 1
    else:
        return start


def quick_sort(elements, start, pivot_index):
    if start < pivot_index:
        partition_index = partition(elements, start, pivot_index)
        # Re-run algo with new pivot
        quick_sort(elements, 0, partition_index - 1)

if __name__ == "__main__":
    elements = [11, 9, 29, 7, 2, 15, 28]
    # i = start at beginning for Lumuto
    quick_sort(elements, 0, len(elements)-1)
    print(elements)
