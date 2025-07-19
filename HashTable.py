#Hash Table From Scratch (Chaining Method)
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    # Hash function
    def _hash(self, key):
        return hash(key) % self.size

    # Insert key-value pair
    def insert(self, key, value):
        idx = self._hash(key)
        for pair in self.table[idx]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[idx].append([key, value])

    # Get value by key
    def get(self, key):
        idx = self._hash(key)
        for pair in self.table[idx]:
            if pair[0] == key:
                return pair[1]
        return None

    # Delete key-value pair
    def delete(self, key):
        idx = self._hash(key)
        for i, pair in enumerate(self.table[idx]):
            if pair[0] == key:
                del self.table[idx][i]
                return True
        return False

    # Check if key exists
    def contains(self, key):
        idx = self._hash(key)
        for pair in self.table[idx]:
            if pair[0] == key:
                return True
        return False

    # Display full table
    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")

# Example Usage
ht = HashTable()

ht.insert("apple", 50)
ht.insert("banana", 30)
ht.insert("orange", 20)

print("Value for 'banana':", ht.get("banana"))

print("\nTable before deleting 'apple':")
ht.display()

ht.delete("apple")

print("\nTable after deleting 'apple':")
ht.display()

print("\nContains 'orange'?", ht.contains("orange"))





#1. Find Non-Repeating Character in a String
def first_non_repeating_char(s):
    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in s:
        if count[char] == 1:
            return char
    return None

# Example
print("First Non-Repeating:", first_non_repeating_char("aabbcdde"))






#2. Check if Two Arrays are Equal (Element-wise, ignoring order)
def are_arrays_equal(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    count1, count2 = {}, {}

    for num in arr1:
        count1[num] = count1.get(num, 0) + 1

    for num in arr2:
        count2[num] = count2.get(num, 0) + 1

    return count1 == count2

# Example
print("Arrays Equal:", are_arrays_equal([1,2,3,4,4], [4,3,2,4,1]))


#3. Count Number of Pairs with Given Sum
def count_pairs_with_sum(arr, target):
    count = {}
    pairs = 0

    for num in arr:
        complement = target - num
        if complement in count:
            pairs += count[complement]
        count[num] = count.get(num, 0) + 1

    return pairs

# Example
print("Pairs with sum 5:", count_pairs_with_sum([1, 5, 7, -1, 5], 6))