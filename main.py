from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix(4, 4)
print "Matrix: "
print_matrix(matrix)
print "Ident: "
ident(matrix)
print_matrix(matrix)
matrix[3][3] = 17.33
print "New matrix:"
print_matrix(matrix)
identity = new_matrix(4, 4)
ident(identity)
matrix_mult(identity, matrix)
m1 = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
m2 = [[1,2],[2,4],[7,8],[9,10]]
m2 = matrix_mult(m1, m2)
print "m2: "
print_matrix(m2)
matrix = [[250, 450, 450, 250], [250, 400, 400, 400], [0, 0, 0, 0], [0, 0, 0, 0]]

draw_lines( matrix, screen, color )
display(screen)
