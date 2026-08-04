def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            print(f"Shifting {arr[j]} to the right") 
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        print(f"Inserted {key} -> {arr}")

    return arr

print(insertion_sort([12, 11, 13, 5, 6]))