import numpy as np
from cpmpy import *


class SetModel:
    def __init__(self, C, A, b):
        self.n_variables = A.shape[1]
        self.n_constraint = A.shape[0]
        self.C = C
        self.A = (A*100).astype(int)
        self.b = (b*100).astype(int)
        self.solution = None

    def get_model(self):
        x = intvar(0, 1000, shape=self.n_variables, name='x')

        model = Model(
            [sum(self.A[i] * x) <= self.b[i] for i in range(self.n_constraint)])

        model.maximize(sum(self.C * x))

        if model.solve():
            self.solution = x.value()
            print(self.solution)
        else:
            print('No solution')


if __name__ == '__main__':
    np.random.seed(1)
    N_ISTANCES = 2
    N_VAR = 3
    N_CONST = 2
    C = np.round(np.random.uniform(low=0, high=1, size=(N_ISTANCES, N_VAR)), 2)
    A = np.round(np.random.uniform(low=0, high=1, size=(N_ISTANCES, N_CONST, N_VAR)), 2)
    b = np.round(np.random.uniform(low=0, high=10, size=(N_ISTANCES, N_CONST)), 2)

    ISTANCE = 1
    PROBLEM = SetModel(C[ISTANCE, :], A[ISTANCE, :, :], b[ISTANCE, :])
    PROBLEM.get_model()
