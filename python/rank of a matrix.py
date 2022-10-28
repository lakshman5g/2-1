import numpy as np
my_matrix = np.array([[1, 0, 0], [0, 4, 0], [0, 0, 3]])
print("Matrix")
for row in my_matrix:
    print(row)
rank = np.linalg.matrix_rank(my_matrix)
print("Rank of the given Matrix is : ",rank)
det=np.linalg.det(my_matrix)
print(int(det))