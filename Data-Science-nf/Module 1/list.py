#1. Write a program to find the largest and smallest elements in a list.  
numbers = [3,1,6,8,1,8,0]
largest=max(numbers)
smallest=min(numbers)
print("largest numbers is:",max(numbers))
print("smallest numbers is:",min(numbers))

#2. Write a program to remove duplicate elements from a list.

numbers = [1, 2, 2, 3, 4, 4, 5]
new_list = []
for i in numbers:
    if i not in new_list:
        new_list.append(i)
print(new_list)
 
#3. Write a program to reverse a list without using built-in reverse functions.

numbers = [1, 2, 3, 4, 5,6,1]
reversed_list = numbers[::-1]
print(reversed_list)

#4. Write a program to count even and odd numbers in a list.

numbers = [2,3,4,5,6,7,81]
even=0
odd=0
for i in numbers:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print("even numbers",even)
print("odd numbers",odd)

#5. Write a program to merge two lists and sort the final list.
 
list1 = [2,3,4,5]
list2 = [8,9,7,6]

list3 = list1+list2
list3.sort()
print("sorted",list3)

#6. Write a program to find the second largest element in a list. 

numbers = [2, 34, 3, 40, 3]
numbers.sort()
print("Second largest element:", numbers[-2])


