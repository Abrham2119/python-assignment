def length():
    print('**Enter 1 for mile to kilometer conversion**')
    print('**Enter 2 for kilometer to mile conversion**')
    num = int(input())
    if num == 1:
        miles = float(input('Enter the length in miles\n'))
        kilometer = miles * 1.609
        print(miles,'miles =',kilometer,'km')
    elif num == 2:
        kilometer = float(input('Enter the length in kilometer\n'))
        miles = kilometer / 1.6
        print(kilometer,'kilometer =',miles,'miles')

def weight():
    print('**Enter 1 for kilogram to pound conversion**')
    print('**Enter 2 for pound to kilogram conversion**')
    num = int(input())
    if num == 1:
        kilogram = float(input('Enter the weight in kilogram\n'))
        pound = kilogram * 2.204
        print(kilogram,'kilogram =',pound,'pound')
    elif num == 2:
        pound = float(input('Enter the weight in pound\n'))
        kilogram = pound / 2.204
        print(pound,'pound =',kilogram,'kilogram')

def time():
    print('**Enter 1 for hour to minutes conversion**')
    print('**Enter 2 for minutes to hour conversion**')
    num = int(input())
    if num == 1:
        hour = float(input('Enter the time in hour\n'))
        minute = hour * 60
        print(hour,'hr =',minute,'minutes')
    elif num == 2:
        minute = float(input('Enter the time in minutes\n'))
        hour = minute / 60
        print(minute,'minutes =',hour,'hour')

print('-----Enter 1 for length conversion------')
print('-----Enter 2 for weight conversion------')
print('-----Enter 3 for time conversion--------')
enteredNo = int(input())
if enteredNo == 1:
    length()
elif enteredNo == 2:
    weight()
elif enteredNo == 3:
    time()
else:
    print('Please choose correctly')

