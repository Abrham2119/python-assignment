digits = input('Enter the 9 digits of ISBN\n')

checksum = 0
for i in range(len(digits)):
    checksum = checksum + int(digits[i])*(i+1)
ISBN = digits + str(checksum%11)
print('The ISBN code is :',ISBN)