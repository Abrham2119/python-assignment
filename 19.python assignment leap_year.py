counter = 0
print('The leap years in 21st century: ')
for i in range(2001,2100):
    if i % 4 == 0:
        counter = counter + 1
        if counter <= 10:
            print(i,end=' ',)
        else:
            print(i)
            counter = 0
        