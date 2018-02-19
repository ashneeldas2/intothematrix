from display import *
from matrix import *


def draw_lines( matrix, screen, color ):
    row1 = matrix[0]
    row2 = matrix[1]
    for i in range(len(row1) - 1): 
        draw_line(row1[i], row2[i], row1[i+1], row2[i+1], screen, color)

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point( matrix, x, y, z=0 ):
    matrix[0].append(x)
    matrix[1].append(y)
    matrix[2].append(z)
    matrix[3].append(1)

def draw_line( x0, y0, x1, y1, screen, color):
    if (x0 > x1): 
        temp = x0
        x0 = x1
        x1 = temp 
        temp = y0
        y0 = y1
        y1 = temp 
    
    x = x0 
    y = y0
    a = y1-y0
    b = -(x1-x0)

    if (b == 0): 
        if y0<y1: 
            while y <= y1: 
                plot(screen, color, x, y)
                y += 1
        else: 
            while y >= y1: 
                plot(screen, color, x, y)
                y -= 1
        return
    
    m = -1.0 * a/b

    if m <= 1 and m >= 0:
        d = 2 * a + b        
        while (x <= x1) :
            plot(screen, color, x, y)
            if d > 0:
                y += 1
                d += 2 * b
            x += 1
            d += 2 * a
    elif m >= -1 and m < 0:
        d = 2 * a - b
        while (x <= x1) :
            plot(screen, color, x, y)
            if d < 0:
                y -= 1
                d -= 2 * b
            x += 1
            d += 2 * a
    elif (m > 1):
        d = a + 2 * b
        while (y <= y1) :
            plot(screen, color, x, y)
            if d < 0:
                x += 1
                d += 2 * a
            y += 1
            d += 2 * b
    elif (m < -1):
        d =  a - 2 * b
        while (y >= y1) :
            plot(screen, color, x, y)
            if d > 0:
                x += 1
                d += 2 * a
            y -= 1
            d -= 2 * b