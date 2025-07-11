
class Student:
    def __init__(self, id = 0, name = '', marks = 0):
        self.id = id
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Id = {self.id}, Name = {self.name}, Marks = {self.marks}"

        
class Node:
    def __init__(self, data = None):
        self.data = data
        self.link = None

    def create_student(self):
        id = int(input("Enter your id: "))
        name = input("Enter your name: ")
        marks = float(input("Enter your marks out of 100: "))
        student = Student(id, name, marks)
        return student
    

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_front(self):
        new_node = Node()
        student = new_node.create_student()
        new_node.data = student

        if self.head == None:
            self.head = self.tail = new_node
            print("New data inserted")
            return
        
        new_node.link = self.head
        self.head = new_node
        print("New data inserted")

    def display(self):
        if self.head == None:
            print("List is Empty")
            return
        
        temp = self.head
        while temp != None:
            print("[", temp.data, "]", "->", end = " ")
            temp = temp.link
        
        print()

    def delete_first(self):
        if self.head == None:
            print("The list is Empty!!")
            return
        
        print("Node deleted at First!!")
        self.head = self.head.link

    def insert_rear(self):
        new_node = Node()
        student = new_node.create_student()
        new_node.data = student

        if self.head == None:
            self.head = self.tail = new_node
            print("New data inserted")
            return
        
        self.tail.link = new_node
        self.tail = new_node
        print("New data inserted")

    def delete_last(self):
        if self.head == None:
            print("The list is Empty!!")
            return
        
        if self.head == self.tail:
            self.head = self.tail = None
            return
        
        temp = self.head

        while temp.link != self.tail:
            temp = temp.link

        temp.link = None
        self.tail = temp
        print("Node deleted at the end!!")

    def peek(self):
        if self.head == None:
            print("List is empty!!")
            return
        
        print("Head =", self.head.data)
        print("Tail =", self.tail.data)
        

if __name__ == '__main__':
    ll = SLL()

    def menu(choice):
        match choice:
            case 1: ll.insert_front(),
            case 2: ll.insert_rear(),
            case 3: ll.delete_first(),
            case 4: ll.delete_last(),
            case 5: ll.display(),
            case 6: ll.peek(),
            case 7: print("Thank You!!"),
            case _: print("Invalid Choice!!")

    while True:
        print("1. Insert Front   2. Insert Rear   3. Delete First   4. Delete Last   5. Display   6. Show Head and Tail   7. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 7:
            print()
            menu(choice)
            print()
            break
        else:
            print()
            menu(choice)
            print()
