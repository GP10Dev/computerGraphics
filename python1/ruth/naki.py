#NAKISOZI RUTH
#20/U/ITE/13666/PE
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def search(self, head, data, index):
        if head.data == data:
            print(index)
        else:
            if head.next:
                return self.search(head.next, data, index+1)
            else:
                raise ValueError("Node not in linked list")

    def print_list(self):
        if self.head is None:
            raise ValueError("List is empty")

        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def size(self):
        if self.head is None:
            return 0
        size = 0
        temp = self.head
        while temp:
            size += 1
            temp = temp.next
        return size

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        print("Added node to the list is: " + str(data))
    def delete(self, data):
        if self.head is None:
            return
        temp = self.head
        if temp.data == data:
            self.head = temp.next
            print("Deleted node is " + str(temp.data))
            return
        while temp.next:
            if temp.next.data == data:
                print("The Node deleted is " + str(temp.next.data))
                temp.next = temp.next.next
                return
            temp = temp.next
        print("Node not found")
    def display_with_spaces(self):
        if self.head is None:
             raise ValueError("List is empty")
        temp = self.head
        while temp:
            print(temp.data, end=", ")
            temp = temp.next
        print()
my_list = LinkedList()
my_list.add(1)
my_list.add(2)
my_list.add(3)
my_list.add(4)
my_list.add(5)
my_list.add(8.5)
my_list.add(6)
my_list.add(11)
my_list.add(3.0)
my_list.display_with_spaces()

my_list.delete(8.5)
my_list.delete(1)
my_list.delete(1)
my_list.display_with_spaces()
