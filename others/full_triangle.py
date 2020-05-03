#full triangle program

import math

def get_vertex():
    x = float(input('please enter x: '))
    y = float(input('please enter y: '))
    return x,y

def get_triangle():
    print("first vertex")
    x1, y1 = get_vertex()
    print("second vertex")
    x2,y2 = get_vertex()
    print("third vertex")
    x3,y3 = get_vertex()    
    return x1, y1, x2, y2, x3, y3


def side_length(x1,y1,x2,y2):
    '''return length of a side (Euclidean
    distance)'''
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def calculate_area(x1,y1,x2,y2,x3,y3):
    '''return area unsing Heron's formula'''
    a = side_length(x1,y1,x2,y2)
    b = side_length(x2,y2,x3,y3)
    c = side_length(x3,y3,x1,y1)
    s = (1/2)*(a+b+c)
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

x1,y1,x2,y2,x3,y3 = get_triangle()
area = calculate_area(x1,y1,x2,y2,x3,y3)
print("Area is: ", area)




