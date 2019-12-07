import numpy as np
import funcoesSegundaQuestao as fs

"""
Dado o sistema:
                 4x  + 3y = 20
                -5x  + 9y = 26
"""

m_list = [[4, 3], [-5, 9]]
A = np.array(m_list)
b = np.array([20, 26])

print(f' Resolução do sistema utilizando Regra de Crame:  {fs.cramer(A, b)}')
print(f' Resolução do sistema utilizando matriz inversa:  {fs.solve(A, b)}')

"""
O mesmo vale para o seguinte sistema:
                4x  + 3y + 2z =  25
               -2x + 2y + 3z  = -10
                3x  -5y  + 2z = -4

"""
C = np.array([[4, 3, 2], [-2, 2, 3], [3, -5, 2]])
d = np.array([25, -10, -4])




print(f' Resolução do sistema utilizando Regra de Crame:  {fs.cramer(C, d)}')

print(f' Resolução do sistema utilizando matriz inversa:  {fs.solve(C, d)}')