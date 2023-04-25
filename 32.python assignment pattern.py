counter = 0
first = 7
for i in range(7):
    for j in range(7-i):
        print(' ',end=' ')
        if j == 7 - i - 1:
            for k in range(i):
                print(i,end=' ')
                i -= 1
            print('')