import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['@','#','$','%','^','&','*','(',')']

print("Welcome to password generator")
n_letters = int(input("enter the number of letters needed : "))
n_numbers = int(input("how many number you needed : "))
n_symbols = int(input("enter the number of symbols needed : "))

# EASY
# password = ""
# for i in range(0,n_letters):
#     password += random.choice(letters)
# for i in range(0,n_numbers):
#     password += random.choice(numbers)
# for i in range(0,n_symbols):
#     password += random.choice(symbols)
#
# print(password)


#hard

password_list = []
for i in range(0,n_letters):
    password_list.append(random.choice(letters))
for i in range(0,n_numbers):
    password_list.append(random.choice(numbers))
for i in range(0,n_symbols):
    password_list.append(random.choice(symbols))

# print(password_list)
random.shuffle(password_list)
# print(password_list)

password_string = ""
for i in password_list:
    password_string += i
print(f"your password generated is : {password_string}")



