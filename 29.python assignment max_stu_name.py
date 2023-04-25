noOfStu = int(input('Enter the number of student\n'))
nameArr = []
scoreArr = []
for i in range(noOfStu):
    name = input('Name: ')
    nameArr.append(name)
    score = int(input('Score: '))
    scoreArr.append(score)

max = scoreArr[0]
index = 0
for i in range(len(nameArr)):
    if scoreArr[i] > max:
        max = scoreArr[i]
        index = i
print(nameArr[index],'scores highest mark')