arr = [4, 5, 3, 1, 2]

def selection_sort():
    length = len(arr)
    for i in range(length - 1):
        min = i
        for j in range(i + 1, length):
            if arr[j] < arr[min]:
                min = j

        arr[min], arr[i] = arr[i], arr[min]

selection_sort()
print(arr)