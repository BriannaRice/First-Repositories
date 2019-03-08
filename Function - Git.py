# 4.13.3:Greetings
# Brianna Rice
# 2.5.19
'''
name = input("What is your name: ")

def greeting():
    print("Hi there " + name + "!")
    print("Nice to meet you ")

greeting()
'''

# 4.13.: Functions and variables
# Brianna Rice
# 2.11.19

x = 10

def print_something():
    x = 3
    print('\r\n',x)

print('\r\n', x)
print_something()

# Brianna Rice
# 2.18.19
# 4.13.6 Functions and Variable pt. 3
def print_number(x):
    print('\n', x)

print_number(13)
print_number(23)


# 4.14.4 name age
# Brianna Rice
# 24.18.19

def name_and_age(name, age):
    print('\n','Hi, my name is', name, 'and I am', str(age), 'years old')

name_and_age('bvcdgf', 41)
name_and_age('vmfkvmfkm', 3)

# 4.14.5: Default Parameter and values
# Brie Rice
# 2.19.19

def print_two_numbers(x,y = 20):
    print('First number:', x)
    print('Second number: ' + str(y))

print_two_numbers(34,54)
print_two_numbers(78)

# 4.14.6: Print some
# Brie Rice
# 2.19.19

def print_some(x,y):
    print(x + y)

print_some(46,62)

# 4.16.3: Enter a number using Try & Except
# Brianna Rice
# 2.20.19
try:
    my_num = int(input('Enter an integer: '))
    print('Your number:', my_num)

except ValueError:
    print('\n''that was not and integer, (:')

# 4.16.4 Enter name and age using try and except rule
# Brianna Rice
# 2.20.19

name = input('Enter name:')
age = 3

try:
    age = int(input('Enter age:'))

except ValueError:
    print('\n''That was not a integer')

print('\n''Name:', name)
print('Age:', age)


# Brianna Rice
# 1.14.19

my_number = 16

print("Guess a number between 1 and 20")
print("")
guess = int(input("Enter a guess:"))

while guess != my_number:
    print("")
    print("Wrong, guess again")
    guess = int(input("Enter a guess:"))

print("")
print("Good job, you got it!")
