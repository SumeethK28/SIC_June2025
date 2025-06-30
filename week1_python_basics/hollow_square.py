# To print Hollow Square

number_of_lines = int(input("Enter the number of lines you want the Hollow Square to be printed: "))

for i in range(1, number_of_lines + 1):  # for each row
    if i == 1 or i == number_of_lines:  # to print full line for first and last row 
        for j in range(1, number_of_lines + 1): 
            print("* ", end = "")
    else:
        for k in range(1, number_of_lines + 1): 
            if k == 1 or k == number_of_lines:  # for remaining lines print only first and last coloumn 
                print("* ", end = "")
            else:
                print("  ", end = "")
    print("")  # for new line