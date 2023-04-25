start = ord('!')
end = ord('~')
counter = 0
i = start
while i <= end:
    print(chr(i), end=' ')
    counter += 1
    i += 1
    if counter == 9:
        print(chr(i))
        counter = 0
    else:
        pass
