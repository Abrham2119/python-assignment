num1 = int(input('Enter the number\n'))
num = num1 + 1
for i in range(2,num+1):
    for j in range(num-i):
        print(' ',end=' ')
    for k in range(1,i-1):
        print(i-k,end=' ')
    for l in range(1,i):
        print(l,end=' ')
    for m in range(num-i):
        print(' ',end=' ')
    print()
    