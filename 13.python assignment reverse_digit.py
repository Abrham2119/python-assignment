digit = input('Enter the no\n')
a = ''
for i in range(1,len(digit)+1):
    a = a + (digit[-i])
print(a)