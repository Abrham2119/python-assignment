def isPrime(num):
    for i in range(0,num):
        if num == 1 or 0:
            print('The number is not prime')
            break
        elif num == 2:
            print('The number is prime')
            break
        elif i > 2 and num % i == 0:
            print('The number is not prime')
            break
        elif num == i+1:
            print('The number is prime')
            break
num = int(input('Enter the number\n'))
isPrime(num)