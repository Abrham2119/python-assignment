def Intersect(m1, b1, m2, b2):
    if m1 == m2:
        print('The lines does\'nt intersect ')
        return 0 # the lines are parallel and don't intersect
    
    x = (b2 - b1) / (m1 - m2) # x-coordinate of the intersection point
    y = m1 * x + b1 # y-coordinate of the intersection point
    
    print(x, y) # return the intersection point as a tuple

m1 = int(input('Enter the first line slope\n'))
m2 = int(input('Enter the second line slope\n'))
b1 = int(input('Enter the first line constant\n'))
b2 = int(input('Enter the second line constant\n'))
Intersect(m1,b1,m2,b2)