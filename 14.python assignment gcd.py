# by Euclid's Algorithm
a = int(input('Enter the first no\n'))
b = int(input('Enter the second no\n'))
arr = [a,b]

if a > b:
    gcd = a
else:
    gcd = b
    
for i in range(gcd):
    if arr[0] > arr[1]:
        arr[0] = arr[0] - arr[1]
        if arr[0] == arr[1]:
            gcd = arr[0]
            break
    elif arr[0] == arr[1]:
        gcd = arr[0]
    else:
        arr[1] = arr[1] - arr[0]
        if arr[1] == arr[0]:
            gcd = arr[1]
            break
print('The GCD of',a,'&',b,'is', gcd) 