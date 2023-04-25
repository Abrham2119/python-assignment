noOfStu = int(input('Enter the number of student\n'))
nameArr = []
scoreArr = []
for i in range(noOfStu):
    name = input('Name: ')
    nameArr.append(name)
    score = int(input('Score: '))
    scoreArr.append(score)

for i in range(len(scoreArr)):
    for j in range(i + 1, len(scoreArr)):
        if scoreArr[i] > scoreArr[j]:
           scoreArr[i], scoreArr[j] = scoreArr[j], scoreArr[i]
print('Max score is:',scoreArr[-1],'\nSecond highest score:',scoreArr[-2])
