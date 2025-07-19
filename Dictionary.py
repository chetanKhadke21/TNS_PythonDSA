# 1.Given a list of numbers, count how many times each number occurs using a dictionary.
numbers = [1, 2, 2, 3, 3, 3, 4]
frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(frequency)

# 2.Find the Key with Maximum Value
marks = {"John": 45, "Emma": 88, "Noah": 77}
topper = max(marks, key=marks.get)
print("Topper is:", topper)


# 3.Merge Two Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1.update(dict2)
print(dict1)

#4. Invert a Dictionary (Swap Keys and Values)
original = {'a': 1, 'b': 2, 'c': 3}
inverted = {}

for key, value in original.items():
    inverted[value] = key

print(inverted)

#5. Check if Two Dictionaries are Equal
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 2, "a": 1}

print(dict1 == dict2)  # True

dict3 = {"a": 2, "b": 1}
print(dict1 == dict3)  # False