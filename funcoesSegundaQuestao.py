import numpy as np

def cramer(A, b):
    solucao = np.zeros((len(b), 1))
    detA = round(np.linalg.det(A), 16)
    if detA != 0:
        for i in range(len(b)):
            B = A.copy()
            B[:, i] = b.transpose()
            detB = round(np.linalg.det(B), 16)
            solucao[i] = (detB / detA)
    else:
        return "Não é possivel resolver sistema!"

    return solucao


def solve(A, b):
    return np.linalg.inv(A).dot(b)
