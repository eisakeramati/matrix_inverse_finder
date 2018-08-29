# matrix_inverse_finder
Linear Algebra project. functions for solving matrix equations and finding inverse of matrices.

The code is a class with different functions.The final purpose of these functions is to find the inverse of the given matrix.

- LU_decomposer() is a function that does the LU decomposition of the given matrix, and stores the value of the L and U matrices.
- each of the equation_u and equation_l fucntions are used to find the solution(lower matrice and upper matrice) needed for the inverse of matrix.they can 
  be used individualy for other purposes too.
- myInverse() is basically a loop used to find solution to Ax=I equation, where in each step uses the linear_sys_solver() to find solution 
  of the above equaiton where the right hand of the equation is one of the columns(vector) of the identity matrix
  
rest are the functions used for my own experiments.
