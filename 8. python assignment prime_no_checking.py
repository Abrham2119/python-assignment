num = int(input('Enter the number\n'))
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
    # elif i+1 == num:
    #     print('The number is prime')
    




# def primenumberCheching(num):
#     if num % (2 or 3 or 5 or 7) == 0 and num != (2 or 3 or 5 or 7) or num < 2:
#         print('It is not prime number')
#     elif num == 2 or 3 or 5 or 7:
#         print('It is prime number')
#     else:
#         print('It is prime number')

# num = int(input('Enter the number\n'))
# primenumberCheching(num)