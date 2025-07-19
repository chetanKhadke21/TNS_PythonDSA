#1. Singly Linked List (from scratch)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Singly Linked List
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head: # is head empty
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

# Example
sll = SinglyLinkedList()
sll.insert_at_end(10)
sll.insert_at_end(20)
sll.insert_at_end(30)
sll.display()


#2. Doubly Linked List (from scratch)
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Doubly Linked List
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next
        print("None")

# Example
dll = DoublyLinkedList()
dll.insert_at_end(100)
dll.insert_at_end(200)
dll.insert_at_end(300)
dll.display()


#3. Circular Singly Linked List (from scratch)
class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None

# Circular Singly Linked List
class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = CNode(data)
        if not self.head:  #if list is empty
            self.head = new_node
            new_node.next = self.head #  to maintain circularity. #In a circular list, even a single node must point to itself.
            return
        curr = self.head  #if list is not empty
        while curr.next != self.head:
            curr = curr.next
        curr.next = new_node #Link the last node to the new node
        new_node.next = self.head #  link new_node.next back to the head to preserve circularity.

    def display(self):
        if not self.head:
            print("Empty List")
            return
        curr = self.head
        while True:
            print(curr.data, end=" -> ")
            curr = curr.next
            if curr == self.head:
                break
        print("(back to head)")

# Example
csll = CircularSinglyLinkedList()
csll.insert_at_end(5)
csll.insert_at_end(10)
csll.insert_at_end(15)
csll.display()


#4. Circular Doubly Linked List (from scratch)
class CDNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Circular Doubly Linked List
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = CDNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node.prev = new_node #maintains both circularity and doubly-linked nature even with one node.
            return
        last = self.head.prev #ircular doubly linked list, the previous of head (head.prev) is the last node.
        last.next = new_node
        new_node.prev = last
        new_node.next = self.head 
        self.head.prev = new_node

    def display(self):
        if not self.head:
            print("Empty List")
            return
        curr = self.head
        while True:
            print(curr.data, end=" <-> ")
            curr = curr.next
            if curr == self.head:
                break
        print("(back to head)")

# Example
cdll = CircularDoublyLinkedList()
cdll.insert_at_end(50)
cdll.insert_at_end(60)
cdll.insert_at_end(70)
cdll.display()




#1. Reverse a Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Create list: 1 -> 2 -> 3 -> None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# Reverse it
new_head = reverse_list(head)

# Print result
curr = new_head
while curr:
    print(curr.data, end=" -> ")
    curr = curr.next
print("None")


#2. Detect a Loop in a Linked List (Floyd’s Cycle Detection)

def has_loop(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Example with no loop
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
print(has_loop(head))  # False

# Example with loop
head.next.next.next = head  # Creating a loop
print(has_loop(head))  # True



#3. Find the Middle Element of a Linked List
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data

# Create list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print(find_middle(head))



#4. Merge Two Sorted Linked Lists
def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 or l2
    return dummy.next

# List1: 1 -> 3 -> 5
a = Node(1)
a.next = Node(3)
a.next.next = Node(5)

# List2: 2 -> 4 -> 6
b = Node(2)
b.next = Node(4)
b.next.next = Node(6)

# Merge and print
merged = merge_sorted_lists(a, b)
curr = merged
while curr:
    print(curr.data, end=" -> ")
    curr = curr.next
print("None")



#5. Remove Duplicates from a Linked List

def remove_duplicates(head):
    seen = set()
    current = head
    prev = None
    while current:
        if current.data in seen:
            prev.next = current.next
        else:
            seen.add(current.data)
            prev = current
        current = current.next

# Create list: 1 -> 2 -> 2 -> 3
head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(3)

remove_duplicates(head)

# Print result
curr = head
while curr:
    print(curr.data, end=" -> ")
    curr = curr.next
print("None")