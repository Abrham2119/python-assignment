num1 = int(input('Enter the number\n'))
num = num1 + 1
for i in range(1,num+1):
    for j in range(num-i):
        print(' ',end=' ')
    for l in range(0,i):
        print(2**l,end=' ')
    for k in range(0,i-1):
        print(2**(i-k-2),end=' ')
    for m in range(num-i):
        print(' ',end=' ')
    print()
    