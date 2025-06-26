# Find the Nth Fibo (HemaChandra) term. Assume 1st 2 terms are 1 and 2

first_term = 1
second_term = 2

nth_number = int(input("Enter the index number to display that particular Fibonacci Term: "))

i = 3

while i <= nth_number:
    third_term = first_term + second_term
    first_term = second_term
    second_term = third_term

    i += 1

print(third_term, "is the", nth_number, end = "" + "th Fibonacci Term!!")

# 1 2 3 5 8 13 21 34 55 89 144