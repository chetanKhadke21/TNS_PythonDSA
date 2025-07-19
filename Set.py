# Remove Duplicates from a List Using Set
numbers = [1, 2, 3, 2, 4, 1, 5]
unique_numbers = list(set(numbers))
print("Unique numbers:", unique_numbers)

#Check if Two Sets Have Common Elements
set1 = {1, 2, 3}
set2 = {4,3, 6}

if set1.intersection(set2):
    print("Yes")
else:
    print("No")

#Find Elements Present in Only One of the Two Sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.symmetric_difference(set2)

print("Elements unique to either set:", result)

#Count the Number of Unique Characters in a String
text = "hello"
unique_chars = set(text)
print("Number of unique characters:", len(unique_chars))

#Check if One Set is a Subset of Another
set1 = {1, 2}
set2 = {1, 2, 3, 4}
print("Is set1 a subset of set2?", set1.issubset(set2))