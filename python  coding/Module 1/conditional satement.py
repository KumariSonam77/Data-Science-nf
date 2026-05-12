#1. Write a program to check whether a year is a leap year or not. 

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

#2. Write a program to find the largest among three numbers using nested conditional statements. 

a = 10
b = 25
c = 15
if a >= b and a >= c:
    print("A is largest")
elif b >= a and b >= c:
    print("B is largest")
else:
    print("C is largest")

# 3. Write a program to check whether a character is an uppercase letter, lowercase letter, digit, or 
# special character. 
char = input("Enter a character: ")

if char.isupper():
    print("Uppercase Letter")
elif char.islower():
    print("Lowercase Letter")
elif char.isdigit():
    print("Digit")
else:
    print("Special Character")


#4. Write a program to calculate electricity bill using different unit slabs. 
units = float(input("Enter units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    bill = (100 * 5) + (200 * 7) + ((units - 300) * 10)

print(f"Total Bill: ${bill}")

#5. Write a program to determine whether a triangle is Equilateral, Isosceles, or Scalene.
x, y, z = 5, 5, 5

if x == y == z:
    print("Equilateral")
elif x == y or y == z or x == z:
    print("Isosceles")
else:
    print("Scalene")
