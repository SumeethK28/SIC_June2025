arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

arr.sort()

def binary_search(low, high, search):
    if low > high:
        return "Element Not Found!!"

    mid = (low + high)//2

    if arr[mid] == search:
        return f"Element found at position {mid}"
    
    elif search < arr[mid]:
        return binary_search(low, mid - 1, search)

    elif search > arr[mid]:
        return binary_search(mid + 1, high, search)

low = 0
high = len(arr) - 1
search = int(input("Enter search element: "))
print(binary_search(low, high, search))