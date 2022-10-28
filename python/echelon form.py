import sympy
  
# find the reduced row echelon form
sympy.Matrix([[4,0,1],[2,0,2],[3,0,3]]).rref()
  
# find the rank of matrix
print("Rank of matrix :",sympy.Matrix([[4,0,1],[2,0,2],[3,0,3]]).rank())