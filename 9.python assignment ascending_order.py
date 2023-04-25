arr = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34]

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] > arr[j]:
           arr[i], arr[j] = arr[j], arr[i]
print (arr)