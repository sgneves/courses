#**************************************************************************************************#
#                                                                                                  #
# 03_Matrix_algebra                                                                                #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Basic Matrix Operations
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2. Matrix Vector Multiplication
import numpy as np

matrix_a = np.array([[0.7,3,9],[1.7,2,9],[0.7,9,2]])
vector_b = np.array([[1.0],[2],[1]])

ab_product = np.dot(matrix_a, vector_b)

#--------------------------------------------------------------------------------------------------#

#%% 3. Matrix Multiplication
matrix_a = np.asarray([
    [0.7, 3],
    [1.7, 2],
    [0.7, 9]
], dtype=np.float32)

matrix_b = np.asarray([
    [113, 3, 10],
    [1, 0, 1],
], dtype=np.float32)

product_ab = np.dot(matrix_a, matrix_b)
print(product_ab)

product_ba = np.dot(matrix_b, matrix_a)
print(product_ba)

#--------------------------------------------------------------------------------------------------#

#%% 4. Matrix Transpose
matrix_a = np.asarray([
    [0.7, 3],
    [1.7, 2],
    [0.7, 9]
], dtype=np.float32)

matrix_b = np.asarray([
    [113, 3, 10],
    [1, 0, 1],
], dtype=np.float32)

transpose_a = np.transpose(matrix_a)
print(transpose_a)

print(np.transpose(transpose_a))

trans_ba = np.dot(np.transpose(matrix_b), np.transpose(matrix_a))

trans_ab = np.dot(np.transpose(matrix_a), np.transpose(matrix_b))

product_ab = np.dot(matrix_a, matrix_b)

print(np.transpose(product_ab))

#--------------------------------------------------------------------------------------------------#

#%% 5. Identity Matrix
i_2 = np.identity(2)

i_3 = np.identity(3)

matrix_33 = np.asarray([
    [0.7, 3],
    [1.7, 2],
    [0.7, 9]
], dtype=np.float32)

matrix_23 = np.asarray([
    [113, 3, 10],
    [1, 0, 1],
], dtype=np.float32)

identity_33 = np.dot(i_3, matrix_33)

identity_23 = np.dot(i_2, matrix_23)

#--------------------------------------------------------------------------------------------------#

#%% 6. Matrix Inverse
matrix_a = np.asarray([
    [1.5, 3],
    [1, 4]
])

def matrix_inverse_two(matrix_22):

    a = matrix_22[0,0]
    b = matrix_22[0,1]
    c = matrix_22[1,0]
    d = matrix_22[1,1]

    return 1 / (a * d - b * c) * np.array([[d,-b],[-c,a]])

inverse_a = matrix_inverse_two(matrix_a)

i_2 = np.dot(inverse_a, matrix_a)
print(i_2)

#--------------------------------------------------------------------------------------------------#

#%% 7. Solving The Matrix Equation
matrix = np.array([[30,-1],[50,-1]])
vector = np.array([[-1000],[-100]])

solution_x = np.dot(np.linalg.inv(matrix), vector)

#--------------------------------------------------------------------------------------------------#

#%% 8. Determinant For Higher Dimensions
matrix_22 = np.asarray([
    [8, 4],
    [4, 2]
])

matrix_33 = np.asarray([
    [1, 1, 1],
    [1, 1, 6],
    [7, 8, 9]
])

det_22 = np.linalg.det(matrix_22)

det_33 = np.linalg.det(matrix_33)

#--------------------------------------------------------------------------------------------------#

#%% 9. Matrix Inverse For Higher Dimensions
# No code
