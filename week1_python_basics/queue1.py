import sys as s

queue_lst = []

def en_queue():
    element = int(input("Enter the element you want to insert: "))
    queue_lst.append(element)
    print(element, "is inserted")

def de_queue():
    if queue_lst:
        element = queue_lst.pop(0)
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

menu = {
    1: en_queue,
    2: de_queue,
    3: display_queue,
    4: exit_program
}

while True:
    print("1. Enqueue   2. Dequeue   3. Display   4. Exit")
    choice = int(input("Enter the desired choice: "))
    menu.get(choice, invalid_input)()