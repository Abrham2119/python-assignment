num = 7
for i in range(num):
    for k in range(0,i):
        print(' ',end=' ')
    for j in range(1,num - i):
        print(j,end=' ')
    print()