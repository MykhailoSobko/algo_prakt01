def selection_sort(arr: list) -> int:
    # Traverse through all array elements
    num_comps = 1
    for i in range(len(arr)):
        num_comps += 1

        # Find the minimum element in remaining unsorted array
        min_idx = i
        num_comps += 1
        for j in range(i + 1, len(arr)):
            num_comps += 2
            if arr[min_idx] > arr[j]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return num_comps


def insertion_sort(arr: list) -> int:
    # Traverse through 1 to len(arr)
    num_comps = 1
    for i in range(1, len(arr)):
        num_comps += 1
        key = arr[i]
        # Move elements of arr[0..i - 1] that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        num_comps += 1
        while j >= 0 and key < arr[j]:
            num_comps += 2
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return num_comps


def merge_sort(arr: list, left: int, right: int) -> int:
    def merge(array: list, left_idx: int, mid_idx: int, right_idx: int) -> int:
        n1 = mid_idx - left_idx + 1
        n2 = right_idx - mid_idx

        # Create temp arrays
        left_arr = [0] * n1
        right_arr = [0] * n2

        # Copy data to temp arrays left_arr[] and right_arr[]
        comps = 1
        for i in range(0, n1):
            comps += 1
            left_arr[i] = arr[left_idx + i]

        comps += 1
        for j in range(0, n2):
            comps += 1
            right_arr[j] = arr[mid_idx + 1 + j]

        # Merge the temp arrays back into arr[left_idx..right_idx]
        i = 0  # Initial index of first subarray
        j = 0  # Initial index of second subarray
        k = left_idx  # Initial index of merged subarray

        comps += 2
        while i < n1 and j < n2:
            comps += 3
            if left_arr[i] <= right_arr[j]:
                array[k] = left_arr[i]
                i += 1
            else:
                array[k] = right_arr[j]
                j += 1
            k += 1

        # Copy the remaining elements of left_arr[], if there are any
        comps += 1
        while i < n1:
            comps += 1
            array[k] = left_arr[i]
            i += 1
            k += 1

        # Copy the remaining elements of right_arr[], if there are any
        comps += 1
        while j < n2:
            comps += 1
            array[k] = right_arr[j]
            j += 1
            k += 1

        return comps

    num_comps = 1
    if left < right:
        # Same as (left + right) // 2, but avoids overflow for
        # large left and right
        mid = left + (right - left) // 2

        # Sort first and second halves
        num_comps += merge_sort(arr, left, mid)
        num_comps += merge_sort(arr, mid + 1, right)
        num_comps += merge(arr, left, mid, right)

    return num_comps


def shell_sort(arr: list) -> int:
    # Start with a big gap, then reduce the gap
    n = len(arr)
    gap = n // 2

    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped
    # order keep adding one more element until the entire array
    # is gap sorted
    num_comps = 1
    while gap > 0:
        num_comps += 2
        for i in range(gap, n):
            num_comps += 1
            # Add arr[i] to the elements that have been gap sorted
            # Save arr[i] in temp and make a hole at position i
            temp = arr[i]

            # Shift earlier gap-sorted elements up until the correct
            # location for arr[i] is found
            j = i
            num_comps += 2
            while j >= gap and arr[j - gap] > temp:
                num_comps += 2
                arr[j] = arr[j - gap]
                j -= gap

            # Put temp (the original arr[i]) in its correct location
            arr[j] = temp
        gap //= 2

    return num_comps
