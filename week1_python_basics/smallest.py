'''
Find smallest of 3 distinct numbers
'''

a, b, c = input("Enter three numbers: ").split()
a = int(a)
b = int(b)
c = int(c)

if a < b and a < c:
    print(a, "is smallest.")
elif b < a and b < c:
    print(b, "is smallest.")
else:
    print(c, "is smallest.")