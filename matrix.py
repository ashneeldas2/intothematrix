import math

def print_matrix( matrix ):
    for i in range(len(matrix)): 
        for j in range(len(matrix[i])): 
            print matrix[i][j],
        print

def ident( matrix ):
    for i in range(len(matrix)): 
        for j in range(len(matrix[i])):
            if i == j: 
                matrix[i][j] = 1
            else: 
                matrix[i][j] = 0

#m1 * m2 -> m2
def matrix_mult( m1, m2 ): 
    result = new_matrix(len(m2[0]), len(m2))
    for i in range(len(m1)):
        for j in range(len(m2[0])): 
            for k in range(len(m2)): 
                result[i][j] += m1[i][k] * m2[k][j]
    return result

def new_matrix(rows, cols):
    m = []
    for c in range( cols ):
        m.append( [] ) 
        for r in range( rows ):
            m[c].append( 0 )
    return m
