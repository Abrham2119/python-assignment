def factorial(num):
    fact = 1
    for i in range(num+1):
        fact *= i+1
    return fact
def sumOfFactorial(number):
    sum = 0
    for i in range(number):
        sum = sum + factorial(i)
    print(sum)

number = int(input('Enter the number: '))
sumOfFactorial(number)