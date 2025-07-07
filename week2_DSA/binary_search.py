arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binary_search(search):
    low = 0
    high = len(arr) - 1

    while True:
        mid = (low + high)//2

        if arr[mid] == search:
            return f"Element found at position {mid}"
        elif search < arr[mid]:
            high = mid - 1
        elif search > arr[mid]:
            low = mid + 1

        if low > high:
            return "Element not found!!"

search = int(input("Enter search element: "))
print(binary_search(search))