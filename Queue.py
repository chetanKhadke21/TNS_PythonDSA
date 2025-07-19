#Queue from scratch

class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue operation
    def enqueue(self, item):
        self.queue += [item]

    # Dequeue operation
    def dequeue(self):
        if not self.isEmpty():
            front_element = self.queue[0]
            self.queue = self.queue[1:]  # remove first element manually
            return front_element
        else:
            return "Queue Underflow"

    # Peek operation
    def peek(self):
        if not self.isEmpty():
            return self.queue[0]
        else:
            return "Queue is empty"

    # isEmpty operation
    def isEmpty(self):
        return len(self.queue) == 0

    # size operation
    def size(self):
        return len(self.queue)

    # display queue
    def display(self):
        return self.queue


# Example usage:
q = Queue()
print("Initial queue:", q.display())

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("Queue after enqueues:", q.display())

print("Front element (peek):", q.peek())

print("Removed element (dequeue):", q.dequeue())
print("Queue after dequeue:", q.display())

print("Is queue empty?", q.isEmpty())
print("Queue size:", q.size())

#1. Implement a Queue Using Two Stacks
class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return "Queue Underflow"
        return self.stack2.pop()

# Example
q = QueueUsingStacks()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())  # 10
print(q.dequeue())  # 20


#2. Generate Binary Numbers from 1 to N

from collections import deque

def generateBinaryNumbers(N):
    result = []
    queue = deque()
    queue.append("1")

    for _ in range(N):
        front = queue.popleft()
        result.append(front)
        queue.append(front + "0")
        queue.append(front + "1")

    return result

# Example
print(generateBinaryNumbers(7))  # ['1', '10', '11', '100', '101']



#3. Reverse a Queue

from collections import deque

def reverseQueue(queue):
    if not queue:
        return
    front = queue.popleft()
    reverseQueue(queue)
    queue.append(front)

# Example
q = deque([10, 20, 30, 40])
reverseQueue(q)
print(list(q))  # [40, 30, 20, 10]