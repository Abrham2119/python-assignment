num = int(input('Enter the number\n'))
factorial = 1
sum = 1
for i in range(10):
    expresions = num ** (i+1) 
    factorial *= (i+1)
    sum += expresions / factorial
print(sum)
