#1. Calculate the sum of two numbers entered by the user
num1 = int(input("Enter a number "))
num2 = int(input("Enter a number "))
add = num1 + num2
print(f"The sum is {add}")

#2. Remove duplicates from a list.
list1 = [1,2,3,3,4,2,5,6]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)

#3. Check if a given number is prime.
num1 = int(input("Enter a number: "))
if num1 <= 1:
    print("Not a prime number")
elif num1 == 2:
    print("Number is a prime number")
else:
    for i in range(2,num1):
        if num1 % i == 0:
            print("Number is not prime")
            break
    else:
        print("Number is a prime number")

#4.Convert a string to uppercase.
inp = input("Enter a string: ").upper()
print(inp)