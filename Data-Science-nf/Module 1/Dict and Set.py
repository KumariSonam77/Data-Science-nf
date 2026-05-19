#1. Write a program to create a dictionary from two lists: one of keys and one of values.

keys = ["name", "age", "city"]
values = ["Sonam", 20, "Delhi"]
my_dict = dict(zip(keys, values))
print(my_dict)

#2. Merge two dictionaries into one

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1 | dict2
print(merged)

#3. Write a program to sort a dictionary by its values.

d = {"a": 3, "b": 1, "c": 2}
sorted_d = sorted(d.values())
print(sorted_d)

#4. Given two sets, check if one set is a subset of another.

set1 = {1, 2}
set2 = {1, 2, 3, 4}
print(set1.issubset(set2))

#5. Write a program to check whether two lists have at least one common element using sets.

list1 = [1, 2, 3]
list2 = [3, 4, 5]
common = set(list1) & set(list2)
if common:
    print("Common element found")
else:
    print("No common element")