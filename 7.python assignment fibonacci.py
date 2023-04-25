def fibonacci(num,first,second,next):
    if num > 2:
        next = first + second
        first = second
        second = next
        num = num - 1
        if num == 2:
            print(next)
            return
        return fibonacci(num,first,second,next)
    elif num == 2:
        next = 1
    elif num == 1:
        next = 0
    print(next)
num = int(input('Enter\n'))
fibonacci(num,0,1,10)

# def fibonacci(num):    
#     i = 2
#     next = 0
#     prev = 0
#     curr = 1
#     if num == 1:
#         next = 0
#     elif num == 2:
#         next = 1
#     else:
#         while i < num:
#             next = prev + curr
#             prev = curr
#             curr = next
#             i = i + 1
#     print(next)
# num = int(input('Enter\n'))
# fibonacci(num)