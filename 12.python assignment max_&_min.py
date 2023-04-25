size = int(input('Enter the size of the list\n'))
arr = []
print('Enter the numbers')
for i in range(size):
    num = int(input())
    arr.append(num)
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] > arr[j]:
           arr[i], arr[j] = arr[j], arr[i]
print ('Min no is: ', arr[0],'Max no is: ',arr[size - 1])