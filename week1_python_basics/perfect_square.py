'''
Check if a +ve integer is Perfect square
First we have to take Square Root of the number and convert it to int, then compare it with original number. 
If True then it is Perfect Square!!
'''


number = int(input("Enter the number: "))

half = int(number**0.5)

if half**2 == number:
    print(number, "is a Perfect Square.")