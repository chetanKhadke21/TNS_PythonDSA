# Stack implementation using a class
class Stack:
    def __init__(self):
        self.stack = []  # internal list to store elements

    # Push operation: Add element at the end
    def push(self, item):
        self.stack += [item]  # concatenation instead of append

    # Pop operation: Remove and return top element
    def pop(self):
        if not self.isEmpty():
            top_element = self.stack[len(self.stack)-1]
            self.stack = self.stack[:-1]  # remove last element manually
            return top_element
        else:
            return "Stack Underflow"

    # Peek operation: Return top element without removing
    def peek(self):
        if not self.isEmpty():
            return self.stack[len(self.stack)-1]
        else:
            return "Stack is empty"

    # isEmpty operation: Check if stack is empty
    def isEmpty(self):
        return len(self.stack) == 0

    # size operation: Return number of elements in stack
    def size(self):
        return len(self.stack)

    # Display stack (for debugging)
    def display(self):
        return self.stack


# Example usage:
s = Stack()
print("Initial Stack:", s.display())

s.push(100)
s.push(260)
s.push(360)
print("Stack after pushes:", s.display())

print("Top element (peek):", s.peek())

print("Removed element (pop):", s.pop())
print("Stack after pop:", s.display())

print("Is stack empty?", s.isEmpty())
print("Stack size:", s.size())





#1. Next Greater Element (NGE) Using Stack
def nextGreaterElement(arr):
    result = {}
    stack = []

    for num in arr:
        # Pop elements from stack if current num is greater
        while stack and stack[-1] < num:
            result[stack.pop()] = num
        stack.append(num)

    # Remaining elements have no greater element
    while stack:
        result[stack.pop()] = -1

    return result

# Test
arr = [4, 5, 2, 25]
print("Next Greater Elements:", nextGreaterElement(arr))


#2. Check for Balanced Parentheses

def isBalanced(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != pairs[char]:
                return "Not Balanced"
            stack.pop()

    return "Balanced" if not stack else "Not Balanced"

# Test cases
print(isBalanced("{[()]}"))   # Balanced
print(isBalanced("{[(])}"))   # Not Balanced


#3. Reverse a String Using Stack
def reverseString(string):
    stack = []

    for char in string:
        stack.append(char)

    reversed_str = ""
    while stack:
        reversed_str += stack.pop()

    return reversed_str

# Test
print(reverseString("hello"))  # olleh



#4. Sort a Stack (Using One More Stack)
def sortStack(original_stack):
    temp_stack = []

    while original_stack:
        temp = original_stack.pop()

        while temp_stack and temp_stack[-1] > temp:
            original_stack.append(temp_stack.pop())

        temp_stack.append(temp)

    return temp_stack

# Test
stack = [34, 3, 31, 98, 92, 23]
sorted_stack = sortStack(stack)
print("Sorted stack:", sorted_stack)

