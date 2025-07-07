arr = [4, 5, 3, 1, 2]

def bubble_sort():
    length = len(arr)
    for i in range(length):
        sorted = True
        for j in range(length - 1 -i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sorted = False
        
        if sorted:
            break

    return arr

print(bubble_sort())