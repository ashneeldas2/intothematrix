from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 255 ]
matrix = new_matrix(4, 4)
print "Matrix: "
print_matrix(matrix)
print "Ident: "
ident(matrix)
print_matrix(matrix)
identity = new_matrix(4, 4)
ident(identity)
matrix_mult(identity, matrix)
m1 = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
print "m1 before multiplying: " 
print_matrix(m1) 
print "m2 before multiplying: "
m2 = [[1,2],[3,4],[5,6],[7,8]]
print_matrix(m2)
m2 = matrix_mult(m1, m2)
print "m2 after multiplying: "
print_matrix(m2)
matrix = [[250, 450, 450, 250], [250, 400, 400, 400], [0, 0, 0, 0], [0, 0, 0, 0]]
add_edge(matrix, 250, 400, 0, 250, 250, 0)
add_edge(matrix, 250, 250, 0, 350, 400, 0)
for i in range(350, 450): 
    add_edge(matrix, 250, 250, 0, i, 400, 0)
draw_lines( matrix, screen, color )
print "translation matrix: "
translate = [[1, 0, 0, -100], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
print_matrix(translate)
print "translating"
matrix = matrix_mult(translate, matrix)
draw_lines(matrix, screen, [0, 0, 255])
print "translating AGAIN!"
matrix = matrix_mult(translate, matrix)
draw_lines(matrix, screen, [255, 0, 0])
translate = [[1, 0, 0, 0], [0, 1, 0, -100], [0, 0, 1, 0], [0, 0, 0, 1]]
matrix = matrix_mult(translate, matrix)
display(screen)
