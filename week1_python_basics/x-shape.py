# to print X-Shape 
import math

number_of_lines = int(input("Enter number of lines you want the x-shape to be printed: "))

"""
*       *
 *     *
  *   *
   * *
    *
   * *
  *   *
 *     *
*       *
[space, star, space, star, space]
[2*i, 1, , 1, 2*i]
"""

upper_limit = math.ceil(number_of_lines/2)
lower_limit = math.floor(number_of_lines/2)

if number_of_lines % 2 != 0:
    for i in range(1, upper_limit + 1):
        for j in range(i - 1):
            print(" ", end = "")
        print("*", end = "")
        for j in range(number_of_lines - i - i):
            print(" ", end = "")
        if i != upper_limit:
            print("*", end = "")
        for j in range(i - 1):
            print(" ", end = "")
        print()

    for i in range(lower_limit):
        for j in range(lower_limit - i - 1):
            print(" ", end  = "")
        print("*", end = "")
        for j in range(2 * i + 1):
            print(" ", end = "")
        print("*", end = "")
        for j in range(lower_limit - i - 1):
            print(" ", end  = "")
        print()
else:
    print("Number of Lines is Even!!")