counter = 0
for i in range(100,200):
    if i % 5 == 0 and i % 6 == 0:
        pass
    elif i % 5 == 0 or i % 6 == 0:
        counter += 1
        if counter < 10:
            print(i,end=' ')
        else:
            print(i)
            counter = 0
# print(i,end='') 