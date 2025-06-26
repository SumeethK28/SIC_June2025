# To Print the Prime numbers in decreasing order between m and n (m < n)

def isPrime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

print("Enter the range in such a way that start range should be less than end range to print it in decreasing order!!")
start_range = int(input("Enter the start range to print the prime numbers: "))
end_range = int(input("Enter the end range where it should stop printing: "))

for i in range(end_range, start_range, -1):
    if isPrime(i):
        print(i, end = " ")