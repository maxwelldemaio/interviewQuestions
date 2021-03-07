def swap(a, b, arr):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp


def partition(elements, start, end):
    """Lumuto partitioning scheme"""
    pivot = elements[end]
    p_index = start

    # Move until we find a number > pivot
    for i in range(start, end):
        if elements[i] <= pivot:
            swap(i, p_index, elements)
            p_index += 1

    swap(p_index, end, elements)

    return p_index
    

def quick_sort(elements, start, end):
    if len(elements) == 1:
        return
    if start < end:
        partition_index = partition(elements, start, end)
        # Re-run algo with new pivot
        quick_sort(elements, 0, partition_index - 1)
        quick_sort(elements, partition_index + 1, end)


if __name__ == "__main__":
    elements = [11, 9, 29, 7, 2, 15, 28]
    # i = start at beginning for Lumuto
    quick_sort(elements, 0, len(elements)-1)
    print(elements)
