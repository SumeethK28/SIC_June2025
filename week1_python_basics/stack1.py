import sys

stack_lst = []

def push():
    element = int(input("Enter the element you want to insert: "))
    stack_lst.append(element)
    print(element, "is inserted!!")

def pop():
    if stack_lst:
        element = stack_lst.pop()
        print(element, "is deleted!!")
    else:
        print("The stack is Empty!!")

def display_stack():
    if stack_lst:
        print("The stack elements are ")
        print(stack_lst)
    else:
        print("Stack is Empty!!")
        
def invalid_input():
    print("Invalid Input")

def exit_program():
    sys.exit("Thank you for your time!!")

menu = {
    1: push,
    2: pop,
    3: display_stack,
    4: exit_program
}

while True:
    print("1. Push   2. Pop   3. Display   4. Exit")
    choice = int(input("Enter the operation you want to perform: "))
    menu.get(choice, invalid_input)()