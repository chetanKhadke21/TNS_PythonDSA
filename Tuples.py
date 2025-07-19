# Given a tuple of numbers and a target element, find and print all indexes where the target element occurs in the tuple.
my_tuple = (10, 20, 30, 20, 40, 20)
target = 20

indexes = []
for i in range(len(my_tuple)):
    if my_tuple[i] == target:
        indexes.append(i)
print(indexes)

# Flatten a Tuple of Tuples
my_tuple = ((1,2),(3,4),(5,6))
flatten_list = []

for i in my_tuple:
    for j in i:
        flatten_list.append(j)
print(flatten_list)  

# Swap First and Last Elements
my_tuple = (10, 20, 30, 40)
temp = list(my_tuple)

temp[0], temp[-1] = temp[-1], temp[0]

new_tuple = tuple(temp)
print(new_tuple)

#Find Second Largest Element
my_tuple = (10, 40, 30, 20, 50)
my_list = list(my_tuple)

my_list.sort()
second_largest = my_list[-2]

print(second_largest)

# Check if Two Tuples are Identical

tuple1 = (10, 257, 30)
tuple2 = (10, 257,30)

print(tuple1 == tuple2) #Python sees that tuple1 and tuple2 are assigned to identical immutable values, so it reuses the same object in memory, For is.


