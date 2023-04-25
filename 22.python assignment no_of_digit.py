def no_of_digit():
    a = input('Enter the no.\n')
    if int(a) >= 0:
        print('The no. you entered has',len(a),'digits')
        return no_of_digit()
    else:
        a = int(a)
        return
no_of_digit()