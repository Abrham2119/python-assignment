decimal = int(input('Enter the number: '))
arr = []
while True:
    if decimal >= 16:
        result = decimal // 16
        remainder = decimal % 16
        decimal = result
        arr.append(remainder)
    elif 0 <= decimal <= 15:
        arr.append(decimal)    
        break
    elif decimal < 0:
        print('Please enter the number greater than 0')
        break
    else:
        remainder = result
        arr.append(remainder)
        break

for i in range(len(arr)):
    if arr[-i-1] == 10:
        arr[-i-1] = 'A'
        print(arr[-i-1],end='')
    elif arr[-i-1] == 11:
        arr[-i-1] = 'B'
        print(arr[-i-1],end='')
    elif arr[-i-1] == 12:
        arr[-i-1] = 'C'
        print(arr[-i-1],end='')
    elif arr[-i-1] == 13:
        arr[-i-1] = 'D'
        print(arr[-i-1],end='')
    elif arr[-i-1] == 14:
        arr[-i-1] = 'E'
        print(arr[-i-1],end='')
    elif arr[-i-1] == 15:
        arr[-i-1] = 'F'
        print(arr[-i-1],end='')
    else:
        print(arr[-i-1],end='')
