#1. Create a Function to Check Whether Two Strings are Anagrams Problem Write a function that accepts two strings and returns True if both are anagrams, otherwise False.

def anagram(a, b):
    if sorted(a) == sorted(b):
        return True
    else:
        return False

print(anagram("listen", "silent"))

#2. Create a Function to Find Second Largest Number in a List Problem Write a function that accepts a list and returns the second largest number.

def second_largest(nums):
    nums.sort()
    return nums[-2]

print(second_largest([10, 20, 30, 40, 50,60]))

#3. Create a Function to Count Vowels in a Sentence Problem Write a function that accepts a sentence and returns the count of each vowel.

def count_vowels(text):
    vowels = "aeiou"
    for i in vowels:
        print(i, "=", text.lower().count(i))
count_vowels("Hello World")

#4. Create a Function to Check Whether a Number is an Armstrong Number Problem

def armstrong(num):
    total = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        total = total + digit ** 3
        temp = temp // 10
    if total == num:
        return True
    else:
        return False
print(armstrong(153))

# 5. Create a Function to Find Common Elements Between Multiple Lists 
# Problem 
# Write a function that accepts three lists and returns common elements. 

def common(list1, list2, list3):
    for i in list1:
        if i in list2 and i in list3:
            print(i)
common([1, 2, 3], [2, 3, 4], [2, 5, 3])