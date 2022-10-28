import numpy as np
import numpy.linalg as la
a = np.array([[1,2],[3,4]])
eigen_values, eigen_vectors = la.eig(a)

print(eigen_values)
print(eigen_vectors)