# To Count number of Prime digits in a number

input_number = int(input("Enter the number to check the count of Prime Digits: "))

temporary = input_number
count = 0

while temporary > 0:
    digit = temporary % 10
    if digit % 2 == 0:
        count += 1
    temporary = temporary // 10

print("The number of Prime Digits are", count)