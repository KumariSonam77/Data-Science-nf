#7. Write a program to check whether an element exists in a tuple.

tuple1=(3,4,5,6)
element=4
if element in tuple1:
    print("element exists in tuple")
else:
    print("element does not exists in tuple")

#8. Write a program to count the occurrence of an element in a tuple.

tuple2=(2,3,4,5,2,6,7)
element=3
count=tuple2.count(element)
print("occurence of an element:",count)

#9. Write a program to sort a list of tuples based on tuple values.

tuple3=[(1,2),(4,3),(2,1),(5,2)]
tuple3.sort()
print(tuple3)

#10. Write a program to convert a tuple into a list and a list into a tuple.
# Tuple to List
t = (2, 3, 4, 5)
print(list(t))
# List to Tuple
l = [2, 3, 4, 5]
print(tuple(l))