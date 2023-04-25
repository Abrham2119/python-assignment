factorial = 1
sum = 1
for i in range(1000):
    expresions = 1 ** (i+1) 
    factorial *= (i+1)
    sum += expresions / factorial
print(sum)
