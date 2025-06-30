import sys as s

queue_lst = []

def en_queue():
    element = int(input("Enter the element you want to insert: "))
    queue_lst.insert(0, element)
    print(element, "is inserted")

def de_queue():
    if queue_lst:
        element = queue_lst.pop()
        print(element, "is deleted")
    else:
        print("Queue is Empty!!")

def display_queue():
    if queue_lst:
        print(queue_lst)
    else:
        print("Queue is Empty!!")

def invalid_input():
    print("Invalid Input!!")

def exit_program():
    s.exit("Thank You!!")

def menu(choice):
    match(choice):
        case 1: en_queue()
        case 2: de_queue()
        case 3: display_queue()
        case 4: exit_program()
        case _: invalid_input()

while True:
    print("1. Enqueue   2. Dequeue   3. Display   4. Exit")
    choice = int(input("Enter the desired choice: "))
    menu(choice)