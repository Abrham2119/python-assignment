noOfStu = int(input('Enter the no of students\n'))
arr = []
counter = 0
print('Enter the scores of ' + str(noOfStu) + ' students')
for i in range(noOfStu):
    a = int(input(str(i+1) + '.'))
    arr.append(a)
    if a > 20:
        counter = counter + 1
print(counter ,'students scored greater than 20')
