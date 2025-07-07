def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

    return arr

def partition(arr, low, high):
    pivot_element = arr[high]
    k = low

    for i in range(low, high):
        if arr[i] < pivot_element:
            arr[i], arr[k] = arr[k], arr[i]
            k += 1

    arr[k], arr[high] = arr[high], arr[k]

    return k

if __name__ == "__main__":
    arr = []
    length = int(input("Enter number of elements: "))
    print("Enter the elements: ")

    for _ in range(length):
        arr.append(int(input()))

    low = 0
    high = len(arr) - 1

    print(quick_sort(arr, low, high))