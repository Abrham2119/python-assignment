num = int(input('Enter the number\n'))
arr = [2]
for j in range(3,num+1):
    for i in range(2,j):
        if j % i == 0:
            break
        elif j == i+1:
            arr.append(j)
            break
print(arr)