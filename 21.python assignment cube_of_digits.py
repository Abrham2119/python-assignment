a = input('Enter the no. between 100 and 10000\n')
sum = 0

if 100 < int(a) < 10000:
    for i in a:
        sum = sum + int(i) ** 3
    print(sum)    
else:
    print('Please enter the no between 100 and 10000')
