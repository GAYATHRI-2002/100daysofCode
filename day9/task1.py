#1. Write a Python program to print "Hello, World!".
print("Hello World")

#2. Write a Python program to check if a given number is even or odd.
num1 = int(input("Enter a number : "))

if num1 > 0:
    if num1 % 2 == 0:
        print(f"{num1} is even number")
    else:
        print(f"{num1} is odd number")
else:
    print("enter a valid number greater than 0")

#3. Calculate the factorial of a given number.
num1 = int(input("Enter a number to find its factorial : "))
fact = 1
for i in range(1,num1+1):
    fact = fact * i
print(f"The factorial of {num1} is : {fact}")

#4. Find the largest among three numbers entered by the user.
def largest(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print(f"{num1} is greatest among the three numbers")
    elif num2 > num1 and num2 > num3:
        print(f"{num2} is greatest among the three numbers")
    else:
        print(f"{num3} is greatest among three numbers")

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
largest(num1,num2,num3)

#5. Write a Python program to print all even numbers from 1 to 20.
for i in range(2,21,2):
    print(i)

# Calculate the sum of all numbers from 1 to a given number.
num1 = int(input("Enter a number: "))
sum1 = 0
for i in range(1,num1+1):
    sum1 += i
print(f"The sum of all numbers from 1 to a given numbers {sum1}")


#6. Write a Python program to check if a given string is a palindrome.
def is_palindrome(string1):
    if string1 == string1[::-1]:
        print(f"The {string1} is palindrome")
    else:
        print("Not palindrome")

string1 = input("Enter a string: ").lower()
is_palindrome(string1)

#7. Count the number of vowels in a given string.
vowels = ["a","e","i","o","u"]
string1 = input("Enter a string: ").lower()
count = 0
for i in string1:
    if i in vowels:
        count += 1
print(f"The number of vowels in {string1} is {count}")

#8. Reverse a given list in-place.
list1 = ["Apple","ant",1,2,4]
list1 = list1[::-1]
list1.reverse()
print(list1)




