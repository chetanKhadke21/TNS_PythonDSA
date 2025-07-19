#You are given a list of integers. Write a Python program to perform the following operations sequentially

List = [10, 20, 30, 40]

#Append the number 100 to the end of the list.
List.append(100)
print(List)

#Insert the number 50 at the 3rd position (index 2).
List.insert(2, 50)
print(List)

#Remove the first occurrence of the number 20.
List.remove(20)
print(List)

#Count how many times 10 appears in the list.
Count = List.count(10)
print(Count)

#Reverse the list.
List.reverse()
print(List)

#Sort the list in ascending order
List.sort()
print(List)

#Find the maximum and minimum values in the list.
max_val = max(List)
print(max_val)

min_val = min(List)
print(min_val)

#Calculate the sum of all elements in the list.
sum_val = sum(List)
print(sum_val)