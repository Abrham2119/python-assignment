print('Enter an int value')
arr = []
while True:
    a = int(input())
    if a == 0:
        break
    else:
        arr.append(a)

posiive_counter = 0
negative_counter = 0
sum = 0

for i in range(len(arr)):
    if arr[i] < 0:
        negative_counter += 1
    elif arr[i] > 0:
        posiive_counter += 1

for i in range(len(arr)):
    sum += arr[i]

average = sum / len(arr)
total = negative_counter + posiive_counter
print('The number of positives is',posiive_counter)
print('The number of negatives is',negative_counter)
print('The total is',total)
print('The average is',average)

    

