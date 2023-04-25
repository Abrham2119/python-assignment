def sum(num1,num2):
    print(num1 + num2) 
def difference(num1,num2):
    print(num1 - num2)
def product(num1,num2):
    print(num1 * num2)
def quotient(num1,num2):
    if num2 != 0:
        print(num1 / num2)
    else:
        print('You can\'t use 0 as a denominator')

print('-----Enter 1 for addition----------')
print('-----Enter 2 for subtraction-------')
print('-----Enter 3 for multiplication----')
print('-----Enter 4 for division----------')

num = int(input())
if num == 1:
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    sum(num1,num2)
elif num == 2:
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    difference(num1,num2)
elif num == 3:
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    product(num1,num2)
elif num == 4:
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    quotient(num1,num2)
else:
    print('Please choose correctly')
