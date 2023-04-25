num = int(input('Enter the number\n'))
arr = [2]
for j in range(3,num+1):
    for i in range(2,j):
        if j % i == 0:
            break
        elif j == i+1:
            arr.append(j)
            break
        
for i in range(len(arr)):
    perfect_no = (2 ** (arr[i] - 1)) * (2 ** arr[i] - 1)  
    if num == perfect_no:
        print(num,'is perfect no.')
        break
    elif i == len(arr) - 1:
        print(num,'is not perfect no.')
