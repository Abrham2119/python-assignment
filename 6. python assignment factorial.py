def factorial(num,product):
    if num > 0:
        product = product * num
        num = num - 1
        if num == 0:
            print(product)
            return
        return factorial(num,product)
    else:
        print('Enter valid number')
    
num = int(input('enter an integer number\n'))
factorial(num,1)
