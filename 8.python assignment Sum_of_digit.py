def sumOfDigit(num):
    newNum = str(num)
    sum = 0
    for i in range(len(newNum)):
        sum = sum + int(newNum[i])
    print(sum) 
    
num = input('Enter the number\n')
sumOfDigit(num)
