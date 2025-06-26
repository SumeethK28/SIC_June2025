'''
Check if a year is Leap year
In order to be a Leap year:
    - The year should be divisible by 4 
    - Even though the year is divisible by 4 still it should not be divisible by 100
    - At Last the year should be divisible by 400
'''

year = int(input("Enter the year: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, "is a Leap Year.")