'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def del_node(self, value):
        #searching value is in first node
        if self.head.data == value:
            tmp = self.head
            self.head = self.head.next
            del tmp
            return value
        #search value
        temp = self.head
        while temp.next:
            temp = temp.next
            if temp.next.data == value:
                tmp = temp.next
                temp.next = temp.next.next
                del tmp
                return value


sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.append(7)
sll.display()


class Node2:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        last.prev = last

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(1.2)
dll.display()


class Node3:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node3(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return None

        data = self.top.data
        self.top = self.top.next
        return data

    def display(self):
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


stack = Stack()
stack.push(8)
stack.push(9)
stack.push(89)
stack.display()
print(stack.pop())
stack.display()
'''
#Завдання 1
#Користувач вводить з клавіатури набір чисел.
#Отримані числа необхідно зберегти в однозв'язний список.
#Після чого потрібно показати меню, в якому запропонувати користувачу набір пунктів:
#1. Додати елемент у список.
#2. Видалити елемент зі списку.
#3. Показати вміст списку.
#4. Перевірити, чи є значення у списку.
#5. Замінити значення у списку.
#В залежності від вибору користувача виконується дія, після чого меню відображається знову.
print("Task 1".center(60, "="))

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def del_node(self, value):
        #searching value is in first node
        if self.head.data == value:
            print(value)
            tmp = self.head
            self.head = self.head.next
            del tmp
            return value
        #search value
        temp = self.head
        while temp.next:
            temp = temp.next
            if temp.data == value:
                tmp = temp.next
                temp.next = temp.next.next
                del tmp
                return value

    def delete(self, del_data):
        current = self.head
        if current and current.data == del_data:
            self.head = current.next
            return
        k = None
        while current and current.data != del_data:
            k = current
            current = current.next
        if current is None:
            return
        k.next = current.next
    def find(self, value):
        temp = self.head
        while temp:
            if temp.data == value:
                return True
            temp = temp.next
        return False

    def replace(self, old_val, new_val):
        temp = self.head
        while temp:
            if temp.data == old_val:
                temp.data = new_val
                return True
            temp = temp.next
        return False

l = [1, 3, 4, 5, 6]

sll = SinglyLinkedList()
for e in l:
    sll.append(e)
while True:
    sw = input("1 - add, 2 - del, 3 - display, 4 - find, 5 - replace, 0 - exit: ")
    if sw == '1':
        val = int(input("Enter the number: "))
        sll.append(val)
    elif sw == '2':
        val = int(input("Enter the number: "))
        sll.del_node(val)
        #sll.delete(val)
    elif sw == '3':
        sll.display()
    elif sw == '4':
        val = int(input("Enter the number: "))
        print(sll.find(val))
    elif sw == '5':
        old_val = int(input("Enter the old number: "))
        new_val = int(input("Enter the new number: "))
        sll.replace(old_val, new_val)
    elif sw == '0':
        break

'''
Завдання 2
Користувач вводить з клавіатури набір рядків.
Отримані рядки необхідно зберегти в двозв'язний список.
Після чого потрібно показати меню, в якому запропонувати користувачу набір пунктів:
1. Додати елемент у список
2. Видалити елемент зі списку
3. Показати елементи списку
4. Перевірити чи є значення в списку
5. Замінити значення в списку
В залежності від вибору – виконується дія, далі знову відображається меню.
'''
print("Task 2".center(60, "="))

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class List_bidirectional(Node):
    def __init__(self):
        self.head = None
        self.tail = None

    def isvalinlist(self, value):
        if self.head.data == value:
            return True
        temp = self.head
        while temp.next:
            temp = temp.next
            if temp.data == value:
                return True
        return False

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node
        new_node.prev = last
        self.tail = new_node
        #self.tail.prev = last

    def display_top(self):
        # print(self.head.data)
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def display_tail(self):
        current = self.tail
        while current:
            print(current.data, end=" -> ")
            current = current.prev
        print("None")

    def del_nodes(self, value):
        #searching value is in first node
        if self.head.data == value:
            tmp = self.head
            self.head = self.head.next
            self.head.prev = None
            del tmp
            return value
        #search value
        current = self.head
        while current.next:
            if current.next.data == value:
                tmp = current.next
                current.next = current.next.next
                if tmp.next is None:
                    self.tail = self.tail.prev
                else:
                    tmp.next.prev = current
                del tmp
            current = current.next
        return value

    def reverse(self, oldvalue, newvalue):
        if self.head.data == oldvalue:
            self.head.data = newvalue
            return oldvalue
        temp = self.head
        while temp.next:
            temp = temp.next
            if temp.next.data == oldvalue:
                temp.next.data = newvalue
                return oldvalue


dll=List_bidirectional()

while True:
    sw = int(input("1 - add, 2 - del, 3 - print, 4 - search, 5 - reverse, 0 - exit: "))
    if sw == 1:
        value = input("Enter the value for adding: ")
        dll.append(value)
    elif sw == 2:
        value = input("Enter the value for deleting: ")
        #sw1 = input(f"Do you want to delete all value = {num}? (y/n)")
        dll.del_nodes(value)
    elif sw == 3:
        sw1 = int(input(f"Do you want to print from first to last - 1 or last to first - 2?"))
        if sw1 == 2:
            dll.display_tail()
        else:
            dll.display_top()
    elif sw == 4:
        value = input("Enter the value for finding: ")
        if dll.isvalinlist(value):
            print(f"'{value}' is in List.")
        else:
            print(f"'{value}' isn't in List.")
    elif sw == 5:
        old = int(input("Enter the num for reversing: "))
        new = int(input("Enter the new value: "))

        dll.reverse(old, new)

    elif sw == 0:
        break
