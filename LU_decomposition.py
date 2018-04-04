import numpy as np


class matrix_handler :
    a=[]
    L=[]
    U=[]
    b=[]
    inv = []

    def __init__(self,given_matrix):
        self.a = given_matrix
        self.U = np.zeros((len(given_matrix), len(given_matrix)))
        self.L = np.eye(len(given_matrix), len(given_matrix))
        self.LU_decomposer()



    def LU_decomposer(self):
        if len(self.a) != len(self.a[0]):
            print("the given matrix is not a square one.")
        else:
            j = 0
            while j < len(self.a[0]):
                for i in range(j + 1, len(self.a)):
                    pivot = -1 * (self.a[i][j] / self.a[j][j])
                    self.a[i] = (self.a[j] * pivot) + self.a[i]
                    self.L[i][j] = -pivot
                j = j + 1
        for i in range(0, len(self.a)):
            self.U[i] = self.a[i]



    def equation_L(self, b):
        size = len(self.L)
        list = []
        for k in range(0, size):
            list += [0]
        for i in range(0, size):
            for j in range(0, i):
                b[i] = b[i] - self.L[i][j] * list[j]
            list[i] = b[i]
        self.b= b




    def equation_U(self):
        size = len(self.U)
        list = []
        for k in range(0, size):
            list += [0]
        for i in range(size - 1, -1, -1):

            for j in range(size - 1, -1, -1):
                self.b[i] = self.b[i] - self.U[i][j] * list[j]
            list[i] = self.b[i] / self.U[i][i]
            self.b[i] = self.b[i] / self.U[i][i]
        self.b = list
        b=self.b
        return b

    def linear_sys_solver(self, t):
        self.equation_L(t)
        return self.equation_U()



    def myInverse(self):
        size = len(self.a)
        right_size = np.eye(size,size)
        for i in range(0,size):
            temp = self.linear_sys_solver(right_size[i])
            self.inv+=[temp]
        self.inv = np.array(self.inv).T.tolist()
        y = np.array([np.array(xi) for xi in self.inv])
        return y


def multiply(X,Y):
    result = [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*Y)] for X_row in X]
    return result

def hilbertMaker(n):
    mat = np.zeros((n, n))
    for i in range(0, n):
        for j in range(0, n):
            mat[i][j] = 1 / (i + j + 1)
    return mat


inverse = np.linalg.inv(hilbertMaker(15))
a = np.array([[1.0, 2.0, 3.0], [5.0, 6.0, 7.0], [9.0, 10.0, 12.0]])
a2 = np.array([[1.0, 2.0, 3.0], [5.0, 6.0, 7.0], [9.0, 10.0, 12.0]])
sys1=matrix_handler(hilbertMaker(15))
mat2=hilbertMaker(15)

b = np.array([[1], [4], [8]])
sys1.myInverse()

print(multiply(inverse, hilbertMaker(15)))



