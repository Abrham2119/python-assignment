arr = [1,20,21,1,0,2,20]
max = arr[0]
count = 2
for i in range(len(arr)):
    if arr[i] > max :
        max = arr[i]
        count =  1
    elif arr[i] == max:
        count += 1
    else:
        pass
print('The largest no is:',max)
print('The occurrence count of the largest no is:',count)